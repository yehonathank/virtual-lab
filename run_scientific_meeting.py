"""Runs a research project with GPT agents."""

import json
from pathlib import Path
from typing import Literal

from openai import OpenAI
from tqdm import trange, tqdm

from prompts import (
    NAME_TO_AGENT,
    scientific_meeting_start_prompt,
    scientific_meeting_team_lead_initial_prompt,
    scientific_meeting_team_lead_intermediate_prompt,
    scientific_meeting_team_lead_final_prompt,
    scientific_meeting_team_member_prompt,
)
from utils import compute_token_cost, count_tokens, get_summary

client = OpenAI()


def run_scientific_meeting(
    team_lead: str,
    team_members: tuple[str, ...],
    agenda: str,
    agenda_questions: tuple[str, ...],
    save_dir: Path,
    save_name: str = "discussion",
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
    num_rounds: int = 3,
    max_tokens: int | None = None,
    temperature: float = 0.2,
    model: Literal["gpt-4o", "gpt-3.5-turbo"] = "gpt-4o",
) -> str:
    """Runs a scientific meeting.

    :param team_lead: The team lead.
    :param team_members: The team members.
    :param agenda: The agenda for the meeting.
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :param save_dir: The directory to save the discussion.
    :param save_name: The name of the discussion file that will be saved.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :param num_rounds: The number of rounds of discussion.
    :param max_tokens: The maximum number of tokens per response.
    :param temperature: The sampling temperature.
    :param model: The OpenAI model to use.
    :return: The summary of the meeting (i.e., the last message).
    """
    # Ensure team members is non-empty
    if not team_members:
        raise ValueError("Team members must include at least one agent.")

    # Ensure team lead is in the team
    if team_members[0] != team_lead:
        raise ValueError("Team lead must be first in the team.")

    # Ensure team members are unique
    if len(set(team_members)) != len(team_members):
        raise ValueError("Team members must be unique.")

    # Ensure all team members are available
    for team_member in team_members:
        if team_member not in NAME_TO_AGENT:
            raise ValueError(f"Missing team member: {team_member}")

    # Set up the discussion with the initial prompt
    discussion = [
        {
            "agent": "User",
            "message": {
                "role": "user",
                "content": scientific_meeting_start_prompt(
                    team_lead=team_lead,
                    team_members=team_members,
                    agenda=agenda,
                    agenda_questions=agenda_questions,
                    summaries=summaries,
                    contexts=contexts,
                    num_rounds=num_rounds,
                ),
            },
        },
    ]

    # Track token counts
    input_token_count = 0
    output_token_count = 0
    max_token_length = 0

    # Loop through rounds
    for round_num in trange(num_rounds + 1, desc="Rounds (+ Summary Round)"):

        # Loop through team members and illicit their response
        for team_member in tqdm(team_members, desc="Team Members"):
            # Special prompt for team lead
            if team_member == team_lead:
                if round_num == 0:
                    prompt = scientific_meeting_team_lead_initial_prompt(
                        team_lead=team_lead
                    )
                elif round_num == num_rounds:
                    prompt = scientific_meeting_team_lead_final_prompt(
                        team_lead=team_lead,
                        agenda=agenda,
                        agenda_questions=agenda_questions,
                    )
                else:
                    prompt = scientific_meeting_team_lead_intermediate_prompt(
                        team_lead=team_lead, round_num=round_num, num_rounds=num_rounds
                    )

            # Prompt for other team members
            else:
                prompt = scientific_meeting_team_member_prompt(
                    team_member=team_member, round_num=round_num, num_rounds=num_rounds
                )

            # Add prompt to discussion along with team member meta prompt
            discussion.append(
                {
                    "agent": "User",
                    "message": {
                        "role": "user",
                        "content": prompt,
                    },
                }
            )

            # Get messages
            messages = [NAME_TO_AGENT[team_member].message] + [
                turn["message"] for turn in discussion
            ]

            # Get the response
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=model,
                stream=False,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            response = chat_completion.choices[0].message.content

            # Update token counts
            new_input_token_count = sum(
                count_tokens(turn["message"]["content"]) for turn in discussion
            )
            new_output_token_count = count_tokens(response)

            input_token_count += new_input_token_count
            output_token_count += new_output_token_count

            max_token_length = max(
                max_token_length, new_input_token_count + new_output_token_count
            )

            # Add the response to the discussion
            discussion.append(
                {
                    "agent": NAME_TO_AGENT[team_member].name,
                    "message": {
                        "role": "assistant",
                        "content": response,
                    },
                }
            )

            # If summary round, only team lead responds
            if round_num == num_rounds:
                break

    # Print token counts and cost
    print(f"Input token count: {input_token_count:,}")
    print(f"Output token count: {output_token_count:,}")
    print(f"Max token length: {max_token_length:,}")

    cost = compute_token_cost(
        model=model,
        input_token_count=input_token_count,
        output_token_count=output_token_count,
    )
    print(f"Cost: ${cost:.2f}")

    # Save the discussion as JSON and Markdown
    save_dir.mkdir(parents=True, exist_ok=True)

    with open(save_dir / f"{save_name}.json", "w") as f:
        json.dump(discussion, f, indent=4)

    with open(save_dir / f"{save_name}.md", "w") as file:
        for turn in discussion:
            file.write(f"## {turn['agent']}\n\n{turn['message']['content']}\n\n")

    # Extract summary
    summary = get_summary(discussion)

    return summary
