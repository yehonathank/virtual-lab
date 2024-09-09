import argparse
import numpy as np
import pandas as pd
from transformers import EsmForMaskedLM, EsmTokenizer
import torch
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
from typing import List, Tuple


class MutationDataset(Dataset):
    def __init__(self, sequence: str, amino_acids: str):
        self.sequence = sequence
        self.amino_acids = amino_acids
        self.mutations = self._generate_mutations()

    def _generate_mutations(self) -> List[Tuple[int, str]]:
        mutations = []
        for pos in range(len(self.sequence)):
            for aa in self.amino_acids:
                if self.sequence[pos] != aa:
                    mutations.append((pos, aa))
        return mutations

    def __len__(self):
        return len(self.mutations)

    def __getitem__(self, idx):
        pos, aa = self.mutations[idx]
        mutated_sequence = self.sequence[:pos] + aa + self.sequence[pos + 1 :]
        return pos, self.sequence[pos], aa, mutated_sequence


def parse_arguments() -> Tuple[str, str, int, int, str]:
    """Parse command-line arguments to get the nanobody sequence and display limit.

    Returns:
        Tuple[str, str, int, int, str]: The input CSV file, nanobody name, batch size, number of top mutations to display, and output CSV file path.
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
        help="Batch size for mutant log-likelihood calculations (default: 16).",
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
        help="Path to save the output CSV file with mutation log-likelihoods.",
    )
    args = parser.parse_args()

    # Validate inputs
    if args.top_n <= 0:
        parser.error("Invalid --top-n value: Must be a positive integer.")
    if args.batch_size <= 0:
        parser.error("Invalid --batch-size value: Must be a positive integer.")

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
        input_csv (str): Path to the CSV file containing nanobody sequences.
        nanobody_name (str): Name of the nanobody to analyze.

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
    seq: str, model, tokenizer, batch_size: int, device: str
) -> List[Tuple[str, int, str, str, float]]:
    """Computes log-likelihood ratios for each possible point mutation in the sequence.

    Args:
        seq (str): The input nanobody sequence.
        model: The ESM model for masked language modeling.
        tokenizer: Tokenizer corresponding to the ESM model.
        batch_size (int): Batch size for processing mutations.
        device (str): Device to run the calculations on (e.g., 'cuda' or 'cpu').

    Returns:
        List[Tuple[str, int, str, str, float]]: A list of tuples containing mutated sequence, position, original amino acid, mutated amino acid, and log-likelihood ratio.
    """
    model.to(device)
    model.eval()

    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    dataset = MutationDataset(seq, amino_acids)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False)

    encoded_input = tokenizer(seq, return_tensors="pt", add_special_tokens=True).to(
        device
    )
    with torch.no_grad():
        original_output = model(**encoded_input)

    log_likelihoods = []

    for batch in tqdm(dataloader, desc="Calculating log-likelihoods"):
        positions, original_aas, mutated_aas, mutated_sequences = batch
        mutated_inputs = tokenizer(
            list(mutated_sequences),
            return_tensors="pt",
            padding=True,
            truncation=True,
            add_special_tokens=True,
        ).to(device)

        with torch.no_grad():
            mutated_outputs = model(**mutated_inputs)

        for i in range(len(mutated_sequences)):
            pos = positions[i].item()
            original_aa = original_aas[i]
            mutated_aa = mutated_aas[i]
            mutated_sequence = mutated_sequences[i]

            original_ll = original_output.logits[
                0, pos + 1, tokenizer.convert_tokens_to_ids(original_aa)
            ].item()
            mutated_ll = mutated_outputs.logits[
                i, pos + 1, tokenizer.convert_tokens_to_ids(mutated_aa)
            ].item()
            ll_ratio = mutated_ll - original_ll

            log_likelihoods.append(
                (mutated_sequence, pos + 1, original_aa, mutated_aa, ll_ratio)
            )

    return sorted(log_likelihoods, key=lambda x: x[4], reverse=True)


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

    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print(
            "Warning: CUDA is not available. Running on CPU may be slow. Consider using a cloud service with GPU support."
        )
        print("For CUDA installation, visit: https://pytorch.org/get-started/locally/")

    try:
        nanobody_sequence = load_nanobody_sequence(input_csv, nanobody_name)
    except Exception as e:
        print(f"Error loading nanobody sequence: {e}")
        return

    print("Computing log-likelihood ratios...")
    mutations = compute_log_likelihood_ratios(
        nanobody_sequence, model, tokenizer, batch_size, device
    )

    if mutations:
        print(
            f"Top {top_n} suggested mutations (mutated_sequence, position, original_aa, mutated_aa, log_likelihood_ratio):"
        )
        for mutation in mutations[:top_n]:
            print(mutation)

        if output_csv:
            try:
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
                print(f"Mutations saved to {output_csv}")
            except Exception as e:
                print(f"Error saving mutations to CSV: {e}")
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
