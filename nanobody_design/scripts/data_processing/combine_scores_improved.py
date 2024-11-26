"""Combines scores from ESM, AlphaFold-Multimer, and Rosetta into a single file using the improved weighted score."""

from pathlib import Path

import numpy as np
import pandas as pd


def combine_scores(
    esm_scores_dir: Path,
    alphafold_scores_dir: Path,
    rosetta_scores_dir: Path,
    nanobody: str,
    spikes: list[str],
    all_save_path: Path,
    top_save_path: Path,
    top_n: int = 10,
    starting_sequence: bool = False,
) -> None:
    """Combines scores from ESM, AlphaFold-Multimer, and Rosetta into a single file  using the improved weighted score.

    :param esm_scores_dir: Path to a directory containing ESM scores.
    :param alphafold_scores_dir: Path to a directory containing AlphaFold-Multimer scores.
    :param rosetta_scores_dir: Path to a directory containing Rosetta scores.
    :param nanobody: Name of the nanobody.
    :param spikes: List of spike names.
    :param all_save_path: Path to save all the combined scores.
    :param top_save_path: Path to save the top N combined scores.
    :param top_n: Number of top sequences to display.
    :param starting_sequence: Whether the sequences are the starting sequences.
    """
    # Load scores from the files
    esm_scores = pd.read_csv(esm_scores_dir / f"{nanobody}.csv")
    alphafold_spike_to_scores = {
        spike: pd.read_csv(alphafold_scores_dir / spike / f"{nanobody}.csv")
        for spike in spikes
    }
    rosetta_spike_to_scores = {
        spike: pd.read_csv(rosetta_scores_dir / spike / f"{nanobody}.csv")
        for spike in spikes
    }

    # Get ESM names
    if starting_sequence:
        names = esm_scores["name"]
        sequences = esm_scores["sequence"]
    else:
        names = [
            f"{name}-{original}{position}{mutant}"
            for name, original, position, mutant in zip(
                esm_scores["name"],
                esm_scores["original_aa"],
                esm_scores["position"],
                esm_scores["mutated_aa"],
            )
        ]
        sequences = esm_scores["mutated_sequence"]

    # Set up new DataFrame with ESM scores
    combined_scores = pd.DataFrame(
        data={
            "name": names,
            "sequence": sequences,
            "log_likelihood_ratio": esm_scores["log_likelihood_ratio"],
        },
    )

    # Merge AlphaFold-Multimer scores
    for spike, alphafold_scores in alphafold_spike_to_scores.items():
        alphafold_scores["name"] = [
            Path(path).parent.name.split("_")[0]
            for path in alphafold_scores["PDB_File"]
        ]
        del alphafold_scores["PDB_File"]

        alphafold_scores.rename(
            columns={
                column: f"{column}_{spike}"
                for column in alphafold_scores.columns
                if column != "name"
            },
            inplace=True,
        )

        combined_scores = combined_scores.merge(alphafold_scores, on="name")

    # Merge Rosetta scores
    for spike, rosetta_scores in rosetta_spike_to_scores.items():
        rosetta_scores["name"] = [
            Path(path).stem.split("_")[0] for path in rosetta_scores["File Name"]
        ]
        del rosetta_scores["File Name"]

        rosetta_scores.rename(
            columns={
                column: f"{column}_{spike}"
                for column in rosetta_scores.columns
                if column != "name"
            },
            inplace=True,
        )

        combined_scores = combined_scores.merge(rosetta_scores, on="name")

    # Compute weighted score
    combined_scores["weighted_score"] = (
        0.2 * combined_scores["log_likelihood_ratio"]
        + 0.4
        * float(
            np.mean([combined_scores[f"Interface_pLDDT_{spike}"] for spike in spikes])
        )
        - 0.4
        * float(np.mean([combined_scores[f"dG_separated_{spike}"] for spike in spikes]))
    )

    # Sort by weighted score
    combined_scores.sort_values(by="weighted_score", ascending=False, inplace=True)

    # Save all scores
    all_save_path.parent.mkdir(parents=True, exist_ok=True)
    combined_scores.to_csv(all_save_path, index=False)

    # Save top N scores
    top_save_path.parent.mkdir(parents=True, exist_ok=True)
    combined_scores.head(top_n).to_csv(top_save_path, index=False)


if __name__ == "__main__":
    from tap import tapify

    tapify(combine_scores)
