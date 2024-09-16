"""Select top-scoring mutated nanobodies for experimental validation."""

from pathlib import Path

import pandas as pd


def select_nanobodies(
    scores_paths: list[Path],
    save_path: Path,
    score_column: str = "weighted_score",
    top_n: int = 24,
) -> None:
    """Select top-scoring mutated nanobodies for experimental validation.

    :param scores_paths: List of paths to CSV score files.
    :param save_path: Path to save the selected nanobodies.
    :param score_column: Column name containing the score to sort by.
    :param top_n: Number of nanobodies to select.
    """
    # Load scores from all files and concatenate
    scores = pd.concat([pd.read_csv(path) for path in scores_paths])

    # Sort by weighted score
    scores.sort_values(by=score_column, ascending=False, inplace=True)

    # Select top nanobodies
    selected_nanobodies = scores.head(top_n)

    # Save selected nanobodies
    save_path.parent.mkdir(parents=True, exist_ok=True)
    selected_nanobodies.to_csv(save_path, index=False)


if __name__ == "__main__":
    from tap import tapify

    tapify(select_nanobodies)
