"""Combines scores from ESM, AlphaFold-Multimer, and Rosetta into a single file."""

from pathlib import Path

import pandas as pd


def combine_scores(
    esm_scores_path: Path,
    alphafold_scores_path: Path,
    rosetta_scores_path: Path,
    save_path: Path,
    top_n: int = 5,
) -> None:
    """Combines scores from ESM, AlphaFold-Multimer, and Rosetta into a single file.

    :param esm_scores_path: Path to a CSV file containing ESM scores.
    :param alphafold_scores_path: Path to a CSV file containing AlphaFold-Multimer scores.
    :param rosetta_scores_path: Path to a CSV file containing Rosetta scores.
    :param save_path: Path to save the combined scores.
    :param top_n: Number of top sequences to display.
    """
    # Load scores from all three files
    esm_scores = pd.read_csv(esm_scores_path)
    alphafold_scores = pd.read_csv(alphafold_scores_path)
    rosetta_scores = pd.read_csv(rosetta_scores_path)

    # Set up new DataFrame with ESM scores
    combined_scores = pd.DataFrame(
        data={
            "name": [
                f"{esm_scores_path.stem}-{original}{position}{mutant}"
                for original, position, mutant in zip(
                    esm_scores["original_aa"],
                    esm_scores["position"],
                    esm_scores["mutated_aa"],
                )
            ],
            "sequence": esm_scores["mutated_sequence"],
            "log_likelihood_ratio": esm_scores["log_likelihood_ratio"],
        },
    )

    # Merge AlphaFold-Multimer scores
    alphafold_scores["name"] = [
        Path(path).parent.name.split("_")[-1] for path in alphafold_scores["PDB_File"]
    ]
    del alphafold_scores["PDB_File"]

    combined_scores = combined_scores.merge(alphafold_scores, on="name")

    # Merge Rosetta scores
    combined_scores = combined_scores.merge(
        rosetta_scores, left_on="name", right_on="File Name"
    )

    # Compute weighted score
    combined_scores["weighted_score"] = (
        0.2 * combined_scores["log_likelihood_ratio"]
        + 0.5 * combined_scores["Interface_pLDDT"]
        - 0.3 * combined_scores["dG_cross"]
    )

    # Sort by weighted score
    combined_scores.sort_values(by="weighted_score", ascending=False, inplace=True)

    # Print names of top N sequences
    print(" ".join(combined_scores["name"].head(top_n)))

    # Save combined scores
    save_path.parent.mkdir(parents=True, exist_ok=True)
    combined_scores.to_csv(save_path, index=False)


if __name__ == "__main__":
    from tap import tapify

    tapify(combine_scores)
