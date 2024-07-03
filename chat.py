"""Script to chat with OpenAI's large language models."""

import json
from pathlib import Path

from openai import OpenAI
from tqdm import trange, tqdm

from prompts import scientific_meeting_start_prompt, TEAM_TO_MESSAGE, TEAM_TO_PROMPT

client = OpenAI()


def run_scientific_meeting(
    team_lead: str,
    team_members: tuple[str],
    agenda: str,
    summaries: tuple[str] = (),
    num_rounds: int = 1,
    max_tokens: int = 4096,
    model: str = "gpt-3.5-turbo",  # TODO: swap for GPT-4o
    save_path: Path = Path("discussion.json"),
) -> None:
    """Runs a scientific meeting."""
    # Ensure team members is non-empty
    if not team_members:
        raise ValueError("Team members must include at least one agent.")

    # Ensure team lead is in the team
    if team_members[0] != team_lead:
        raise ValueError("Team lead must be first in the team.")

    # Ensure team members are unique
    if len(set(team_members)) != len(team_members):
        raise ValueError("Team members must be unique.")

    # Ensure all team members have prompts
    for team_member in team_members:
        if team_member not in TEAM_TO_PROMPT:
            raise ValueError(f"No prompt found for team member: {team_member}")

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

    # Loop through rounds and team members and illicit their responses
    for _ in trange(num_rounds, desc="Rounds"):
        for team_member in tqdm(team_members, desc="Team Members"):
            # Prompt team member for a response
            discussion.append(
                {
                    "role": "user",
                    "content": f"{team_member}, please provide your thoughts based on the discussion so far and based on your expertise, goal, and role.",
                }
            )
            messages = [TEAM_TO_MESSAGE[team_member]] + discussion

            # Get the response
            chat_completion = client.chat.completions.create(
                messages=messages,
                model=model,
                stream=False,
                temperature=0,
                seed=0,
                max_tokens=max_tokens,
            )
            response = chat_completion.choices[0].message.content

            # Add the response to the discussion
            discussion.append(
                {
                    "role": "assistant",
                    "content": f"{team_member}: {response}",
                }
            )

    # Ask team lead to summarize the discussion
    discussion.append(
        {
            "role": "user",
            "content": f"{team_lead}, please summarize this meeting in one paragraph for reference in future discussions. Then, provide a specific recommendation regarding the agenda based on team member feedback and your expert judgment.",
        }
    )
    messages = [TEAM_TO_MESSAGE[team_lead]] + discussion

    # Get the response
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        stream=False,
        temperature=0,
        seed=0,
        max_tokens=max_tokens,
    )
    response = chat_completion.choices[0].message.content

    # Add the response to the discussion
    discussion.append(
        {
            "role": "assistant",
            "content": f"{team_lead}: {response}",
        }
    )

    # Save the discussion as JSON
    save_path.parent.mkdir(parents=True, exist_ok=True)

    with open(save_path, "w") as f:
        json.dump(discussion, f, indent=4)


if __name__ == "__main__":
    run_scientific_meeting(
        team_lead="Principal Investigator",
        team_members=tuple(TEAM_TO_PROMPT.keys()),
        agenda="We are interesting in peptide-based drug discovery. Please select an appropriate target for the development of a novel peptide drug.",
    )
