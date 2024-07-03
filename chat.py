"""Script to chat with OpenAI's large language models."""

import json
from pathlib import Path

from openai import OpenAI
from tqdm import trange, tqdm

from prompts import (
    PROJECT_SELECTION_PROMPT,
    scientific_meeting_start_prompt,
    scientific_meeting_team_lead_initial_prompt,
    scientific_meeting_team_lead_intermediate_prompt,
    scientific_meeting_team_lead_final_prompt,
    scientific_meeting_team_member_prompt,
    TARGET_SELECTION_PROMPT,
    TEAM_TO_MESSAGE,
    TEAM_TO_PROMPT,
)
from utils import compute_token_cost, count_tokens, load_summaries

client = OpenAI()


def run_scientific_meeting(
    team_lead: str,
    team_members: tuple[str],
    agenda: str,
    save_dir: Path,
    summaries: tuple[str] = (),
    num_rounds: int = 2,
    max_tokens: int | None = None,
    model: str = "gpt-4o",
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

    # Track token counts
    input_token_count = 0
    output_token_count = 0

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
                messages=[TEAM_TO_MESSAGE[team_member]] + discussion,
                model=model,
                stream=False,
                temperature=0,
                seed=0,
                max_tokens=max_tokens,
            )
            response = chat_completion.choices[0].message.content

            # Update token counts
            input_token_count += sum(
                count_tokens(turn["content"]) for turn in discussion
            )
            output_token_count += count_tokens(response)

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

    cost = compute_token_cost(
        model=model,
        input_token_count=input_token_count,
        output_token_count=output_token_count,
    )
    print(f"Cost: ${cost:.2f}")

    # Save the discussion as JSON and Markdown
    save_dir.mkdir(parents=True, exist_ok=True)

    with open(save_dir / "discussion.json", "w") as f:
        json.dump(discussion, f, indent=4)

    with open(save_dir / "discussion.md", "w") as file:
        for message in discussion:
            role = message["role"]
            content = message["content"]
            file.write(f"## {role.capitalize()}\n\n{content}\n\n")


if __name__ == "__main__":
    team_lead = "Principal Investigator"
    team_members = tuple(TEAM_TO_PROMPT.keys())

    # run_scientific_meeting(
    #     team_lead=team_lead,
    #     team_members=team_members,
    #     agenda=PROJECT_SELECTION_PROMPT,
    #     save_path=Path("discussion.json"),
    # )

    summaries = load_summaries([Path("discussions/project_selection/discussion.json")])

    run_scientific_meeting(
        team_lead=team_lead,
        team_members=team_members,
        agenda=TARGET_SELECTION_PROMPT,
        summaries=summaries,
        save_dir=Path("discussions/target_selection"),
    )
