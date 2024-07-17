"""Runs an individual meeting with an LLM agent."""

import time
from pathlib import Path
from typing import Literal

from openai import OpenAI

from agent import Agent
from prompts import individual_meeting_start_prompt
from utils import get_summary, print_cost_and_time, save_meeting, update_token_counts

client = OpenAI()


def run_individual_meeting(
    team_member: Agent,
    agenda: str,
    save_dir: Path,
    save_name: str = "discussion",
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
    max_tokens: int | None = None,
    temperature: float = 0.2,
    model: Literal["gpt-4o", "gpt-3.5-turbo"] = "gpt-4o",
) -> str:
    """Runs an individual meeting with an LLM agent.

    :param team_member: The team member.
    :param agenda: The agenda for the meeting.
    :param save_dir: The directory to save the discussion.
    :param save_name: The name of the discussion file that will be saved.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :param max_tokens: The maximum number of tokens per response.
    :param temperature: The sampling temperature.
    :param model: The OpenAI model to use.
    :return: The summary of the meeting (i.e., the last message).
    """
    # Start timing the meeting
    start_time = time.time()

    # Set up the discussion with the initial prompt
    discussion = [
        {
            "agent": "User",
            "message": {
                "role": "user",
                "content": individual_meeting_start_prompt(
                    team_member=team_member,
                    agenda=agenda,
                    summaries=summaries,
                    contexts=contexts,
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

    # Get the response
    chat_completion = client.chat.completions.create(
        messages=[team_member.message] + [turn["message"] for turn in discussion],
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
            "agent": team_member.title,
            "message": {
                "role": "assistant",
                "content": response,
            },
        }
    )

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

    # Extract summary
    summary = get_summary(discussion)

    return summary
