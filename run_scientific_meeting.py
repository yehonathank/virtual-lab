"""Runs a scientific meeting with LLM agents."""

import time
from pathlib import Path
from typing import Literal

from openai import OpenAI
from tqdm import trange, tqdm

from constants import CONSISTENT_TEMPERATURE, PUBMED_TOOL_DESCRIPTION
from prompts import (
    Agent,
    scientific_meeting_start_prompt,
    scientific_meeting_team_lead_initial_prompt,
    scientific_meeting_team_lead_intermediate_prompt,
    scientific_meeting_team_lead_final_prompt,
    scientific_meeting_team_member_prompt,
)
from utils import (
    convert_messages_to_discussion,
    count_discussion_tokens,
    count_tokens,
    get_messages,
    get_summary,
    print_cost_and_time,
    run_tools,
    save_meeting,
)

client = OpenAI()


def run_scientific_meeting(
    team_lead: Agent,
    team_members: tuple[Agent, ...],
    agenda: str,
    save_dir: Path,
    save_name: str = "discussion",
    agenda_questions: tuple[str, ...] = (),
    agenda_rules: tuple[str, ...] = (),
    summaries: tuple[str, ...] = (),
    contexts: tuple[str, ...] = (),
    num_rounds: int = 3,
    temperature: float = CONSISTENT_TEMPERATURE,
    model: Literal["gpt-4o", "gpt-3.5-turbo"] = "gpt-4o",
    return_summary: bool = False,
) -> str | None:
    """Runs a scientific meeting with LLM agents.

    :param team_lead: The team lead.
    :param team_members: The team members.
    :param agenda: The agenda for the meeting.
    :param save_dir: The directory to save the discussion.
    :param save_name: The name of the discussion file that will be saved.
    :param agenda_questions: The agenda questions to answer by the end of the meeting.
    :param agenda_rules: The rules for the meeting.
    :param summaries: The summaries of previous meetings.
    :param contexts: The contexts for the meeting.
    :param num_rounds: The number of rounds of discussion.
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

    # Set up assistants
    agent_to_assistant = {
        agent: client.beta.assistants.create(
            name=agent.title,
            instructions=agent.prompt,
            tools=[PUBMED_TOOL_DESCRIPTION],
            model=model,
        )
        for agent in team
    }

    # Map assistant IDs to agents
    assistant_id_to_title = {
        assistant.id: agent.title for agent, assistant in agent_to_assistant.items()
    }

    # Set up tool token count
    tool_token_count = 0

    # Set up the thread
    thread = client.beta.threads.create()

    # Set up the discussion with the initial prompt
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=scientific_meeting_start_prompt(
            team_lead=team_lead,
            team_members=team_members,
            agenda=agenda,
            agenda_questions=agenda_questions,
            agenda_rules=agenda_rules,
            summaries=summaries,
            contexts=contexts,
            num_rounds=num_rounds,
        ),
    )

    # Loop through rounds
    for round_index in trange(num_rounds + 1, desc="Rounds (+ Summary Round)"):
        round_num = round_index + 1

        # Loop through team and elicit responses
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
                        agenda_rules=agenda_rules,
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

                # Update tool token count
                tool_token_count += sum(
                    count_tokens(tool_output["output"]) for tool_output in tool_outputs
                )

                # Submit the tool outputs
                run = client.beta.threads.runs.submit_tool_outputs_and_poll(
                    thread_id=thread.id, run_id=run.id, tool_outputs=tool_outputs
                )

            # Check run status
            if run.status != "completed":
                raise ValueError(f"Run failed: {run.status}")

            # If summary round, only team lead responds
            if round_index == num_rounds:
                break

    # Get messages from the discussion
    messages = get_messages(client=client, thread_id=thread.id)

    # Convert messages to discussion format
    discussion = convert_messages_to_discussion(
        messages=messages, assistant_id_to_title=assistant_id_to_title
    )

    # Count discussion tokens
    token_counts = count_discussion_tokens(discussion=discussion)

    # Add tool token count to total token count
    token_counts["tool"] = tool_token_count

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
