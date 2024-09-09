import argparse
import pandas as pd
import numpy as np
from transformers import EsmForMaskedLM, EsmTokenizer
import torch
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
from typing import List, Tuple


class MutationDataset(Dataset):
    """Custom Dataset for batching mutation sequences."""

    def __init__(self, sequences: List[str]):
        self.sequences = sequences

    def __len__(self):
        return len(self.sequences)

    def __getitem__(self, idx):
        return self.sequences[idx]


def parse_arguments() -> Tuple[str, str, int, int, str]:
    """Parse command-line arguments to get the nanobody sequence, batch size, and output file location.

    Returns:
        Tuple[str, str, int, int, str]: The input CSV file, nanobody name, batch size, number of top mutations to display, and output file location.
    """
    parser = argparse.ArgumentParser(
        description="Identify promising point mutations in a nanobody sequence using ESM log-likelihoods."
    )
    parser.add_argument(
        "input_csv",
        type=str,
        help="Path to the CSV file containing nanobody sequences.",
    )
    parser.add_argument(
        "nanobody_name", type=str, help="Name of the nanobody to analyze."
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=16,
        help="Batch size for mutation calculations (default: 16).",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=10,
        help="Number of top mutations to display (default: 10). Must be a positive integer.",
    )
    parser.add_argument(
        "--output_csv",
        type=str,
        required=True,
        help="Path to save the output CSV file with mutation log-likelihoods.",
    )
    args = parser.parse_args()

    # Validate inputs
    if args.batch_size <= 0:
        parser.error("Invalid --batch-size value: Must be a positive integer.")
    if args.top_n <= 0:
        parser.error("Invalid --top-n value: Must be a positive integer.")

    return (
        args.input_csv,
        args.nanobody_name,
        args.batch_size,
        args.top_n,
        args.output_csv,
    )


def load_nanobody_sequence(input_csv: str, nanobody_name: str) -> str:
    """Load the nanobody sequence from a CSV file based on the nanobody name.

    Args:
        input_csv (str): Path to the CSV file.
        nanobody_name (str): Name of the nanobody.

    Returns:
        str: The amino acid sequence of the nanobody.
    """
    df = pd.read_csv(input_csv)
    sequence_row = df[df["name"] == nanobody_name]
    if sequence_row.empty:
        raise ValueError(
            f"Nanobody with name '{nanobody_name}' not found in the CSV file."
        )
    return sequence_row.iloc[0]["sequence"]


def compute_log_likelihood_ratios(
    seq: str, model, tokenizer, batch_size: int
) -> List[Tuple[str, int, str, str, float]]:
    """Computes log-likelihood ratios for each possible point mutation in the sequence.

    Args:
        seq (str): The input nanobody sequence.
        model: The ESM model for masked language modeling.
        tokenizer: Tokenizer corresponding to the ESM model.
        batch_size (int): Batch size for processing mutations.

    Returns:
        List[Tuple[str, int, str, str, float]]: A list of tuples containing mutated sequence, position, original amino acid, mutated amino acid, and log-likelihood ratio.
    """
    try:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        encoded_input = tokenizer(seq, return_tensors="pt", add_special_tokens=True).to(
            device
        )
        original_output = model(**encoded_input)

        log_likelihoods = []
        amino_acids = "ACDEFGHIKLMNPQRSTVWY"
        mutation_sequences = []

        for pos in range(1, len(seq) + 1):  # Skip [CLS] token which is at index 0
            for aa in amino_acids:
                if seq[pos - 1] == aa:
                    continue
                mutated_sequence = seq[: pos - 1] + aa + seq[pos:]
                mutation_sequences.append((mutated_sequence, pos, seq[pos - 1], aa))

        mutation_dataset = MutationDataset([m[0] for m in mutation_sequences])
        mutation_loader = DataLoader(
            mutation_dataset, batch_size=batch_size, shuffle=False
        )

        for batch in tqdm(mutation_loader, desc="Calculating mutations"):
            mutated_inputs = tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                add_special_tokens=True,
            ).to(device)
            mutated_outputs = model(**mutated_inputs)

            for i, (mutated_sequence, pos, original_aa, mutated_aa) in enumerate(
                mutation_sequences
            ):
                original_ll = original_output.logits[
                    0, pos, tokenizer.convert_tokens_to_ids(seq[pos - 1])
                ].item()
                mutated_ll = mutated_outputs.logits[
                    i, pos, tokenizer.convert_tokens_to_ids(mutated_aa)
                ].item()
                ll_ratio = mutated_ll - original_ll
                log_likelihoods.append(
                    (mutated_sequence, pos, original_aa, mutated_aa, ll_ratio)
                )

        return sorted(log_likelihoods, key=lambda x: x[4], reverse=True)
    except Exception as e:
        print(
            f"An error occurred during computation: {e}. Please ensure your sequence is valid and model is correctly loaded."
        )
        return []


def main():
    input_csv, nanobody_name, batch_size, top_n, output_csv = parse_arguments()

    try:
        print("Loading model and tokenizer...")
        model = EsmForMaskedLM.from_pretrained("facebook/esm1b_t33_650M_UR50S")
        tokenizer = EsmTokenizer.from_pretrained("facebook/esm1b_t33_650M_UR50S")
    except Exception as e:
        print(
            f"Error loading model or tokenizer: {e}. Ensure you have installed 'transformers' and 'torch'."
        )
        print("Installation steps: pip install transformers torch")
        return

    if not torch.cuda.is_available():
        print(
            "Warning: CUDA is not available. Running on CPU may be slow. Consider using a cloud service with GPU support."
        )
        print("For CUDA installation, visit: https://pytorch.org/get-started/locally/")

    try:
        print("Loading nanobody sequence...")
        nanobody_sequence = load_nanobody_sequence(input_csv, nanobody_name)
    except ValueError as e:
        print(e)
        return

    print("Computing log-likelihood ratios...")
    mutations = compute_log_likelihood_ratios(
        nanobody_sequence, model, tokenizer, batch_size
    )

    if mutations:
        print(
            f"Top {top_n} suggested mutations (mutated_sequence, position, original_aa, mutated_aa, log_likelihood_ratio):"
        )
        for mutation in mutations[:top_n]:
            print(mutation)

        # Save results to CSV
        print(f"Saving results to {output_csv}...")
        pd.DataFrame(
            mutations,
            columns=[
                "mutated_sequence",
                "position",
                "original_aa",
                "mutated_aa",
                "log_likelihood_ratio",
            ],
        ).to_csv(output_csv, index=False)
    else:
        print(
            "No mutations could be computed. Please check your input sequence and model."
        )

    print("\nInterpretation:")
    print(
        "Log-likelihood ratios indicate the relative likelihood of mutations improving binding affinity."
    )
    print(
        "Higher positive values suggest potentially beneficial mutations, suitable for further experimental validation."
    )
    print(
        "Consider the biological context, such as structural data or known functional regions, when prioritizing mutations for testing."
    )


if __name__ == "__main__":
    main()
