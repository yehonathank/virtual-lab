"""Pair SARS-CoV-2 spike protein sequences with nanobody sequences (fasta format)."""

from pathlib import Path

from Bio import SeqIO
from itertools import product
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def pair_spike_nanobody(
    spike_path: Path,
    nanobody_path: Path,
    save_dir: Path,
) -> None:
    """Pair SARS-CoV-2 spike protein sequences with nanobody sequences (fasta format).

    :param spike_path: Path to the spike protein sequences (fasta format).
    :param nanobody_path: Path to the nanobody sequences (fasta format).
    :param save_dir: Directory to save the paired sequences.
    """
    # Load sequences from both files
    spike_sequences = list(SeqIO.parse(spike_path, "fasta"))
    nanobody_sequences = list(SeqIO.parse(nanobody_path, "fasta"))

    # Make save directory
    save_dir.mkdir(parents=True, exist_ok=True)

    # Pair spike protein sequences with nanobody sequences
    for spike_seq, nanobody_seq in product(spike_sequences, nanobody_sequences):
        merged_record = SeqRecord(
            Seq(f"{spike_seq.seq}:{nanobody_seq.seq}"),
            id=f"{spike_seq.id}:{nanobody_seq.id}",
            description="",
        )

        # Write the merged sequence to a new FASTA file
        with open(save_dir / f"{spike_seq.id}_{nanobody_seq.id}.fasta", "w") as output_handle:
            SeqIO.write(merged_record, output_handle, "fasta")


if __name__ == "__main__":
    from tap import tapify

    tapify(pair_spike_nanobody)
