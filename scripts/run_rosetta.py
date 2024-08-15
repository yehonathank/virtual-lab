import os
import subprocess
import logging
from typing import List

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_rosetta_antibody_protocol(
    antibody_seq: str, antigen_pdb: str, output_dir: str, rosetta_opts: str
) -> float:
    """
    Run RosettaAntibody protocol for a given antibody sequence and antigen structure.

    :param antibody_seq: Antibody sequence (string)
    :param antigen_pdb: Path to the antigen PDB file
    :param output_dir: Directory to store the output files
    :param rosetta_opts: Additional options for Rosetta
    :return: Binding affinity score (float)
    """
    # Create a temporary directory for this antibody sequence
    try:
        seq_dir = os.path.join(output_dir, antibody_seq)
        os.makedirs(seq_dir, exist_ok=True)
    except OSError as e:
        logging.error(f"Error creating directory {seq_dir}: {e}")
        return float("inf")

    # Write sequence to a fasta file
    fasta_file = os.path.join(seq_dir, "antibody.fasta")
    try:
        with open(fasta_file, "w") as f:
            f.write(f">antibody\n{antibody_seq}\n")
    except IOError as e:
        logging.error(f"Error writing FASTA file {fasta_file}: {e}")
        return float("inf")

    # Define the RosettaAntibody command
    rosetta_command = [
        "rosetta_scripts.default.linuxgccrelease",
        "-parser:protocol",
        "antibody_design.xml",
        "-parser:script_vars",
        f"antibody_fasta={fasta_file}",
        f"antigen_pdb={antigen_pdb}",
    ] + rosetta_opts.split()

    try:
        # Run the Rosetta command
        process = subprocess.run(
            rosetta_command, cwd=seq_dir, capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running RosettaScript for {antibody_seq}: {e.stderr}")
        return float("inf")  # Return a high score to indicate failure

    # Parse the output score
    score_file = os.path.join(seq_dir, "score.sc")
    try:
        with open(score_file, "r") as f:
            lines = f.readlines()
            if len(lines) > 1:
                header = lines[0].split()
                score_index = header.index(
                    "total_score"
                )  # Dynamically find the score column
                score = float(lines[1].split()[score_index])
            else:
                score = float("inf")
    except (FileNotFoundError, IndexError, ValueError) as e:
        logging.error(f"Error parsing score for {antibody_seq}: {e}")
        score = float("inf")

    return score


def rank_antibodies(
    antibody_seqs: List[str], antigen_pdb: str, output_dir: str, rosetta_opts: str
) -> List[str]:
    """
    Rank antibody sequences based on their binding affinity and structural stability.

    :param antibody_seqs: List of antibody sequences
    :param antigen_pdb: Path to the antigen PDB file
    :param output_dir: Directory to store the output files
    :param rosetta_opts: Additional options for Rosetta
    :return: List of antibody sequences ranked by binding affinity
    """
    scores = {}
    for seq in antibody_seqs:
        score = run_rosetta_antibody_protocol(
            seq, antigen_pdb, output_dir, rosetta_opts
        )
        scores[seq] = score
        if score == float("inf"):
            logging.info(f"Skipping sequence {seq} due to errors.")

    # Sort sequences by their scores
    ranked_sequences = sorted(scores, key=scores.get)
    return ranked_sequences


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Rank antibody sequences based on binding affinity using RosettaAntibody."
    )
    parser.add_argument(
        "--antibody_seqs",
        type=str,
        nargs="+",
        required=True,
        help="List of antibody sequences",
    )
    parser.add_argument(
        "--antigen_pdb", type=str, required=True, help="Path to the antigen PDB file"
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Directory to store the output files",
    )
    parser.add_argument(
        "--rosetta_opts", type=str, default="", help="Additional options for Rosetta"
    )

    args = parser.parse_args()

    ranked_sequences = rank_antibodies(
        args.antibody_seqs, args.antigen_pdb, args.output_dir, args.rosetta_opts
    )
    logging.info("Ranked Antibody Sequences:")
    for rank, seq in enumerate(ranked_sequences, start=1):
        print(f"{rank}. {seq}")
