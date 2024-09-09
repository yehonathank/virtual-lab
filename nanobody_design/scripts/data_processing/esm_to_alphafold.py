"""Convert ESM mutated nanobody sequences spike-nanobody sequences for input to AlphaFold."""

from pathlib import Path

import pandas as pd
from Bio import SeqIO
from itertools import product
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def esm_to_alphafold(
    spike_sequences_path: Path,
    nanobody_sequences_path: Path,
    save_dir: Path,
    top_n: int = 10,
    spike_sequence_col: str = "rbd",
    spike_name_col: str = "name",
    nanobody_sequence_col: str = "mutated_sequence",
    nanobody_pos_col: str = "position",
    nanobodoy_original_aa_col: str = "original_aa",
    nanobody_mutated_aa_col: str = "mutated_aa",
    nanobody_llr_col: str = "log_likelihood_ratio",
) -> None:
    """Convert ESM mutated nanobody sequences spike-nanobody sequences for input to AlphaFold

    :param spike_sequences_path: Path to a CSV file containing spike protein sequences.
    :param nanobody_sequences_path: Path to a CSV file containing mutated nanobody sequences from ESM.
    :param save_dir: Directory to save the paired nanobody-spike sequences for input to AlphaFold.
    :param top_n: Number of top mutations to display.
    :param spike_sequence_col: Column name for the spike protein sequence in the CSV file.
    :param spike_name_col: Column name for the spike protein name in the CSV file.
    :param nanobody_sequence_col: Column name for the nanobody sequence in the CSV file.
    :param nanobody_pos_col: Column name for the nanobody mutation position in the CSV file.
    :param nanobodoy_original_aa_col: Column name for the original amino acid in the nanobody mutation in the CSV file.
    :param nanobody_mutated_aa_col: Column name for the mutant amino acid in the nanobody mutation in the CSV file.
    :param nanobody_llr_col: Column name for the log-likelihood ratio in the nanobody mutation in the CSV file.
    """
    # Load sequences from both files
    spike = pd.read_csv(spike_sequences_path)
    nanobody = pd.read_csv(nanobody_sequences_path)

    # Limit the number of top mutations to display
    nanobody = nanobody.sort_values(by=nanobody_llr_col, ascending=False).head(top_n)

    # Get nanobody name
    nanobody_name = nanobody_sequences_path.stem

    # Make save directory
    save_dir.mkdir(parents=True, exist_ok=True)

    # Pair spike protein sequences with nanobody sequences
    for spike_index, nanobody_index in product(range(len(spike)), range(len(nanobody))):
        # Get spike sequence and name
        spike_seq = spike[spike_sequence_col].iloc[spike_index]
        spike_name = spike[spike_name_col].iloc[spike_index]

        # Get nanobody sequence and name
        nanobody_seq = nanobody[nanobody_sequence_col].iloc[nanobody_index]
        nanobody_position = nanobody[nanobody_pos_col].iloc[nanobody_index]
        nanobody_original_aa = nanobody[nanobodoy_original_aa_col].iloc[nanobody_index]
        nanobody_mutant_aa = nanobody[nanobody_mutated_aa_col].iloc[nanobody_index]
        nanobody_mutant_name = f"{nanobody_name}_{nanobody_original_aa}{nanobody_position}{nanobody_mutant_aa}"

        complex_name = f"{spike_name}_{nanobody_mutant_name}"
        merged_record = SeqRecord(
            Seq(f"{spike_seq}:{nanobody_seq}"), id=complex_name, description=""
        )

        # Write the merged sequence to a new FASTA file
        with open(save_dir / f"{complex_name}.fasta", "w") as output_handle:
            SeqIO.write(merged_record, output_handle, "fasta")


if __name__ == "__main__":
    from tap import tapify

    tapify(esm_to_alphafold)
