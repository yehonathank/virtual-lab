"""Script to display a discussion saved as JSON."""

import json
from pathlib import Path


def display_discussion(discussion_path: Path = Path("discussion.json")) -> None:
    """Display a discussion saved as JSON."""
    with open(discussion_path, "r") as file:
        discussion = json.load(file)

    for turn in discussion:
        print(turn["content"] + "\n\n")


if __name__ == "__main__":
    display_discussion()
