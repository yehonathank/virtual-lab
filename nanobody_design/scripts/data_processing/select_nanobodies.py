"""Select top-scoring mutated nanobodies for experimental validation."""

from pathlib import Path

import pandas as pd


def select_nanobodies(
    score_path_pattern: str,
    round_nums: list[int],
    save_path: Path,
    score_column: str = "weighted_score",
    top_n: int = 24,
) -> None:
    """Select top-scoring mutated nanobodies for experimental validation.

    :param score_path_pattern: The pattern to use to find score files by replacing "{round_num}" with the round number.
    :param round_nums: List of round numbers to process.
    :param save_path: Path to save the selected nanobodies.
    :param score_column: Column name containing the score to sort by.
    :param top_n: Number of nanobodies to select.
    """
    # Load scores from all files and concatenate
    scores = pd.concat(
        [
            pd.read_csv(score_path_pattern.format(round_num=round_num)).assign(
                round_num=round_num
            )
            for round_num in round_nums
        ]
    )

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
