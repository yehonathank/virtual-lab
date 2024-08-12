"""Runs a scientific meeting with LLM agents."""

import time
from pathlib import Path
from typing import Literal

from openai import OpenAI
from tqdm import trange, tqdm

from prompts import (
    Agent,
    scientific_meeting_start_prompt,
    scientific_meeting_team_lead_initial_prompt,
    scientific_meeting_team_lead_intermediate_prompt,
    scientific_meeting_team_lead_final_prompt,
    scientific_meeting_team_member_prompt,
)
from utils import get_summary, print_cost_and_time, save_meeting, update_token_counts

client = OpenAI()


def run_scientific_meeting(
    team_lead: Agent,
    team_members: tuple[Agent, ...],
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
    return_summary: bool = False,
) -> str | None:
    """Runs a scientific meeting with LLM agents.

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
    :param return_summary: Whether to return the summary of the meeting.
    :return: The summary of the meeting (i.e., the last message) if return_summary is True, else None.
    """
    # Start timing the meeting
    start_time = time.time()

    # Ensure team members is non-empty
    if len(team_members) == 0:
        raise ValueError("Team members must include at least one agent.")

    # Ensure team lead is separate from the team members
    if team_lead in team_members:
        raise ValueError("Team lead must not be in the team members.")

    # Ensure team members are unique
    if len(set(team_members)) != len(team_members):
        raise ValueError("Team members must be unique.")

    # Set up team
    team = [team_lead] + list(team_members)

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
    token_counts = {
        "input": 0,
        "output": 0,
        "max": 0,
    }

    # Loop through rounds
    for round_index in trange(num_rounds + 1, desc="Rounds (+ Summary Round)"):
        round_num = round_index + 1

        # Loop through team and illicit their response
        for agent in tqdm(team, desc="Team"):
            # Special prompt for team lead
            if agent == team_lead:
                if round_index == 0:
                    prompt = scientific_meeting_team_lead_initial_prompt(
                        team_lead=team_lead
                    )
                elif round_index == num_rounds:
                    prompt = scientific_meeting_team_lead_final_prompt(
                        team_lead=team_lead,
                        agenda=agenda,
                        agenda_questions=agenda_questions,
                    )
                else:
                    prompt = scientific_meeting_team_lead_intermediate_prompt(
                        team_lead=team_lead,
                        round_num=round_num - 1,
                        num_rounds=num_rounds,
                    )

            # Prompt for other team members
            else:
                prompt = scientific_meeting_team_member_prompt(
                    team_member=agent, round_num=round_num, num_rounds=num_rounds
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

            # Get the response
            chat_completion = client.chat.completions.create(
                messages=[agent.message] + [turn["message"] for turn in discussion],
                model=model,
                stream=False,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            response = chat_completion.choices[0].message.content

            # Update token counts
            update_token_counts(
                token_counts=token_counts,
                discussion=discussion,
                response=response,
            )

            # Add the response to the discussion
            discussion.append(
                {
                    "agent": agent.title,
                    "message": {
                        "role": "assistant",
                        "content": response,
                    },
                }
            )

            # If summary round, only team lead responds
            if round_index == num_rounds:
                break

    # Print cost and time
    print_cost_and_time(
        token_counts=token_counts,
        model=model,
        elapsed_time=time.time() - start_time,
    )

    # Save the discussion as JSON and Markdown
    save_meeting(
        save_dir=save_dir,
        save_name=save_name,
        discussion=discussion,
    )

    # Optionally, return summary
    if return_summary:
        return get_summary(discussion)
