"""Runs an individual meeting with an LLM agent."""

import time
from pathlib import Path
from typing import Literal

from openai import OpenAI
from tqdm import trange, tqdm

from agent import Agent
from prompts import (
    individual_meeting_agent_prompt,
    individual_meeting_critic_prompt,
    individual_meeting_start_prompt,
    SCIENTIFIC_CRITIC,
)
from utils import get_summary, print_cost_and_time, save_meeting, update_token_counts

client = OpenAI()


def run_individual_meeting(
    team_member: Agent,
    agenda: str,
    save_dir: Path,
    save_name: str = "discussion",
    agenda_questions: tuple[str, ...] = (),
    agenda_rules: tuple[str, ...] = (),
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
    num_critiques: int = 0,
    max_tokens: int | None = None,
    temperature: float = 0.2,
    model: Literal["gpt-4o", "gpt-3.5-turbo"] = "gpt-4o",
    return_summary: bool = False,
) -> str:
    """Runs an individual meeting with an LLM agent.

    :param team_member: The team member.
    :param agenda: The agenda for the meeting.
    :param save_dir: The directory to save the discussion.
    :param save_name: The name of the discussion file that will be saved.
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :param agenda_rules: The rules for the meeting.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :param num_critiques: The number of critiques and agent rewrites.
    :param max_tokens: The maximum number of tokens per response.
    :param temperature: The sampling temperature.
    :param model: The OpenAI model to use.
    :param return_summary: Whether to return the summary of the meeting.
    :return: The summary of the meeting (i.e., the last message) if return_summary is True, else None.
    """
    # Start timing the meeting
    start_time = time.time()

    # Set up the discussion
    discussion = []

    # Track token counts
    token_counts = {
        "input": 0,
        "output": 0,
        "max": 0,
    }

    # Loop through critiques plus one final round
    for round_index in trange(num_critiques + 1, desc="Critiques (+ Final Round)", leave=False):
        # Set up agents with special case for final round (no critique)
        if round_index == num_critiques:
            agents = [team_member]
        else:
            agents = [team_member, SCIENTIFIC_CRITIC]

        # Loop through agents
        for agent in tqdm(agents, desc="Agents", leave=False):
            # Add user prompt based on agent and round number
            if agent == SCIENTIFIC_CRITIC:
                prompt = individual_meeting_critic_prompt(
                    critic=SCIENTIFIC_CRITIC, agent=team_member
                )
            else:
                if round_index == 0:
                    prompt = individual_meeting_start_prompt(
                        team_member=team_member,
                        agenda=agenda,
                        agenda_questions=agenda_questions,
                        agenda_rules=agenda_rules,
                        summaries=summaries,
                        contexts=contexts,
                    )
                else:
                    prompt = individual_meeting_agent_prompt(
                        critic=SCIENTIFIC_CRITIC, agent=team_member
                    )

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
