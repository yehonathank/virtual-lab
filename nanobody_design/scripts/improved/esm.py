import argparse
import numpy as np
import pandas as pd
from transformers import EsmForMaskedLM, EsmTokenizer
import torch
from typing import List, Tuple
from tqdm import tqdm
import os


def parse_arguments() -> Tuple[str, int, int, str]:
    """Parse command-line arguments to get the CSV file, batch size, and display limit.

    Returns:
        Tuple[str, int, int, str]: The input CSV file path, batch size, number of top mutations to display, and save directory.
    """
    parser = argparse.ArgumentParser(
        description="Identify promising point mutations in nanobody sequences using ESM log-likelihoods."
    )
    parser.add_argument(
        "csv_file",
        type=str,
        help='Path to the CSV file containing nanobody sequences with columns "sequence" and "name".',
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
        "--save-dir",
        type=str,
        required=True,
        help="Directory to save the results CSV files.",
    )
    args = parser.parse_args()

    # Validate inputs
    if args.batch_size <= 0:
        parser.error("Invalid --batch-size value: Must be a positive integer.")
    if args.top_n <= 0:
        parser.error("Invalid --top-n value: Must be a positive integer.")
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    return args.csv_file, args.batch_size, args.top_n, args.save_dir


def compute_log_likelihood_ratios(
    seq: str, model, tokenizer, batch_size: int
) -> List[Tuple[str, int, str, str, float]]:
    """Computes log-likelihood ratios for each possible point mutation in the sequence.

    Args:
        seq (str): The input nanobody sequence.
        model: The ESM model for masked language modeling.
        tokenizer: Tokenizer corresponding to the ESM model.
        batch_size (int): The batch size for processing mutations.

    Returns:
        List[Tuple[str, int, str, str, float]]: A list of tuples containing mutated sequence, position, original amino acid, mutated amino acid, and log-likelihood ratio.
    """
    try:
        encoded_input = tokenizer(seq, return_tensors="pt", add_special_tokens=True).to(
            "cuda"
        )
        original_output = model(**encoded_input)

        log_likelihoods = []
        amino_acids = "ACDEFGHIKLMNPQRSTVWY"
        mutations = []

        for pos in range(1, len(seq) + 1):  # Skip [CLS] token which is at index 0
            for aa in amino_acids:
                if seq[pos - 1] == aa:
                    continue
                mutated_sequence = seq[: pos - 1] + aa + seq[pos:]
                mutations.append((mutated_sequence, pos, seq[pos - 1], aa))

        for i in tqdm(
            range(0, len(mutations), batch_size), desc="Processing mutations"
        ):
            batch_mutations = mutations[i : i + batch_size]
            mutated_sequences = [m[0] for m in batch_mutations]
            mutated_inputs = tokenizer(
                mutated_sequences,
                return_tensors="pt",
                padding=True,
                truncation=True,
                add_special_tokens=True,
            ).to("cuda")
            mutated_outputs = model(**mutated_inputs)

            for j, (mutated_sequence, pos, original_aa, mutated_aa) in enumerate(
                batch_mutations
            ):
                original_ll = original_output.logits[
                    0, pos, tokenizer.convert_tokens_to_ids(seq[pos - 1])
                ].item()
                mutated_ll = mutated_outputs.logits[
                    j, pos, tokenizer.convert_tokens_to_ids(mutated_aa)
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
    csv_file, batch_size, top_n, save_dir = parse_arguments()

    try:
        print("Loading model and tokenizer...")
        model = EsmForMaskedLM.from_pretrained("facebook/esm1b_t33_650M_UR50S").to(
            "cuda"
        )
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
        sequences_df = pd.read_csv(csv_file)
    except Exception as e:
        print(
            f"Error reading CSV file: {e}. Ensure the file exists and is in the correct format."
        )
        return

    for _, row in sequences_df.iterrows():
        nanobody_sequence = row["sequence"]
        nanobody_name = row["name"]

        print(f"Computing log-likelihood ratios for {nanobody_name}...")
        mutations = compute_log_likelihood_ratios(
            nanobody_sequence, model, tokenizer, batch_size
        )

        if mutations:
            output_file = os.path.join(save_dir, f"{nanobody_name}.csv")
            with open(output_file, "w") as f:
                f.write(
                    "mutated_sequence,position,original_aa,mutated_aa,log_likelihood_ratio\n"
                )
                for mutation in mutations:
                    f.write(
                        f"{mutation[0]},{mutation[1]},{mutation[2]},{mutation[3]},{mutation[4]}\n"
                    )
            print(f"Results saved to {output_file}")
        else:
            print(
                f"No mutations could be computed for {nanobody_name}. Please check your input sequence and model."
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
