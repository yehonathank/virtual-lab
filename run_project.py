"""Runs a research project with GPT agents."""

import json
from pathlib import Path
from typing import Literal

from openai import OpenAI
from tqdm import trange, tqdm

from prompts import (
    NAME_TO_AGENT,
    PROJECT_SELECTION_PROMPT,
    scientific_meeting_start_prompt,
    scientific_meeting_team_lead_initial_prompt,
    scientific_meeting_team_lead_intermediate_prompt,
    scientific_meeting_team_lead_final_prompt,
    scientific_meeting_team_member_prompt,
    TARGET_SELECTION_PROMPT,
)
from utils import compute_token_cost, count_tokens

client = OpenAI()


def run_scientific_meeting(
    team_lead: str,
    team_members: tuple[str, ...],
    agenda: str,
    save_dir: Path,
    save_name: str = "discussion",
    summaries: tuple[str, ...] = (),
    num_rounds: int = 3,
    max_tokens: int | None = None,
    model: Literal["gpt-4o", "gpt-3.5-turbo"] = "gpt-4o",
) -> str:
    """Runs a scientific meeting.

    :param team_lead: The team lead.
    :param team_members: The team members.
    :param agenda: The agenda for the meeting.
    :param save_dir: The directory to save the discussion.
    :param save_name: The name of the discussion file that will be saved.
    :param summaries: The summaries of previous meetings.
    :param num_rounds: The number of rounds of discussion.
    :param max_tokens: The maximum number of tokens per response.
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
            "role": "user",
            "content": scientific_meeting_start_prompt(
                team_lead=team_lead,
                team_members=team_members,
                agenda=agenda,
                summaries=summaries,
                num_rounds=num_rounds,
            ),
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
                    prompt = scientific_meeting_team_lead_initial_prompt(team_lead)
                elif round_num == num_rounds:
                    prompt = scientific_meeting_team_lead_final_prompt(team_lead)
                else:
                    prompt = scientific_meeting_team_lead_intermediate_prompt(team_lead)

            # Prompt for other team members
            else:
                prompt = scientific_meeting_team_member_prompt(team_member)

            # Add prompt to discussion along with team member meta prompt
            discussion.append(
                {
                    "role": "user",
                    "content": prompt,
                }
            )

            # Get the response
            chat_completion = client.chat.completions.create(
                messages=[NAME_TO_AGENT[team_member].message] + discussion,
                model=model,
                stream=False,
                temperature=0,
                seed=0,
                max_tokens=max_tokens,
            )
            response = chat_completion.choices[0].message.content

            # Update token counts
            new_input_token_count = sum(
                count_tokens(turn["content"]) for turn in discussion
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
                    "role": "assistant",
                    "content": response,
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
        for message in discussion:
            role = message["role"]  # TODO: replace with agent name
            content = message["content"]
            file.write(f"## {role.capitalize()}\n\n{content}\n\n")

    # Extract summary
    summary = discussion[-1]["content"]

    return summary


def run_project(
    save_dir: Path,
    save_name: str = "discussion",
    num_rounds: int = 3,
    model: Literal["gpt-4o", "gpt-3.5-turbo"] = "gpt-4o",
) -> None:
    """Runs a research project with GPT agents.

    :param save_dir: The directory to save the discussion.
    :param save_name: The name of the discussion file that will be saved.
    :param num_rounds: The number of rounds of discussion.
    :param model: The OpenAI model to use.
    """
    # Set up the team
    team_lead = "Principal Investigator"
    team_members = tuple(NAME_TO_AGENT.keys())

    # Project selection meeting
    project_selection_summary = run_scientific_meeting(
        team_lead=team_lead,
        team_members=team_members,
        agenda=PROJECT_SELECTION_PROMPT,
        save_dir=save_dir / "project_selection",
        save_name=save_name,
        num_rounds=num_rounds,
        model=model,
    )

    # Target selection meeting
    target_selection_summary = run_scientific_meeting(
        team_lead=team_lead,
        team_members=team_members,
        agenda=TARGET_SELECTION_PROMPT,
        summaries=(project_selection_summary,),
        save_dir=save_dir / "target_selection",
        save_name=save_name,
        num_rounds=num_rounds,
        model=model,
    )


if __name__ == "__main__":
    from tap import tapify

    tapify(run_project)
