"""Runs an individual meeting with an LLM agent."""

import time
from pathlib import Path
from typing import Literal

from openai import OpenAI
from tqdm import trange, tqdm

from agent import Agent
from constants import CONSISTENT_TEMPERATURE, PUBMED_TOOL_DESCRIPTION
from prompts import (
    individual_meeting_agent_prompt,
    individual_meeting_critic_prompt,
    individual_meeting_start_prompt,
    SCIENTIFIC_CRITIC,
)
from utils import (
    convert_messages_to_discussion,
    count_discussion_tokens,
    get_messages,
    get_summary,
    print_cost_and_time,
    run_tools,
    save_meeting,
)

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
    temperature: float = CONSISTENT_TEMPERATURE,
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
    :param temperature: The sampling temperature.
    :param model: The OpenAI model to use.
    :param return_summary: Whether to return the summary of the meeting.
    :return: The summary of the meeting (i.e., the last message) if return_summary is True, else None.
    """
    # Start timing the meeting
    start_time = time.time()

    # Set up team
    team = [team_member] + [SCIENTIFIC_CRITIC]

    # Set up the assistants
    agent_to_assistant = {
        agent: client.beta.assistants.create(
            name=agent.title,
            instructions=agent.prompt,
            # tools=[PUBMED_TOOL_DESCRIPTION],  # TODO: turn on PubMed search
            model=model,
        )
        for agent in team
    }

    # Map assistant IDs to agents
    assistant_id_to_title = {
        assistant.id: agent.title for agent, assistant in agent_to_assistant.items()
    }

    # Set up the thread
    thread = client.beta.threads.create()

    # Loop through critiques plus one final round
    for round_index in trange(num_critiques + 1, desc="Critiques (+ Final Round)"):
        # Loop through team and elicit responses
        for agent in tqdm(team, desc="Team"):
            # Prompt based on agent and round number
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

            # Create message from user to agent
            client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=prompt,
            )

            # Run the agent
            run = client.beta.threads.runs.create_and_poll(
                thread_id=thread.id,
                assistant_id=agent_to_assistant[agent].id,
                model=model,
                temperature=temperature,
            )

            # Check if run requires action
            if run.status == "requires_action":
                # Run the tools
                tool_outputs = run_tools(run=run)

                # Submit the tool outputs
                run = client.beta.threads.runs.submit_tool_outputs_and_poll(
                    thread_id=thread.id, run_id=run.id, tool_outputs=tool_outputs
                )

            # Check run status
            if run.status != "completed":
                raise ValueError(f"Run failed: {run.status}")

            # If summary round, only team member responds
            if round_index == num_critiques:
                break

    # Get messages from the discussion
    messages = get_messages(client=client, thread_id=thread.id)

    # Convert messages to discussion format
    discussion = convert_messages_to_discussion(
        messages=messages, assistant_id_to_title=assistant_id_to_title
    )

    # Count discussion tokens
    token_counts = count_discussion_tokens(discussion=discussion)

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
