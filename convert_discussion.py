"""Script to display a discussion saved as JSON."""

import json
from pathlib import Path


def convert_discussion(discussion_path: Path, save_path: Path) -> None:
    """Convert the discussion from JSON to Markdown.

    :param discussion_path: Path to the JSON file containing the discussion.
    :param save_path: Path to save the Markdown file.
    """
    with open(discussion_path, "r") as file:
        discussion = json.load(file)

    with open(save_path, "w") as file:
        for message in discussion:
            role = message["role"]
            content = message["content"]
            file.write(f"## {role.capitalize()}\n\n{content}\n\n")


if __name__ == "__main__":
    from tap import tapify

    tapify(convert_discussion)
