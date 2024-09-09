import argparse
from transformers import EsmForMaskedLM, EsmTokenizer
import torch
from typing import List, Tuple
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

class MutationDataset(Dataset):
    def __init__(self, seq: str, amino_acids: str):
        self.seq = seq
        self.amino_acids = amino_acids
        self.mutations = [
            (pos, aa) for pos in range(len(seq))
            for aa in amino_acids if seq[pos] != aa
        ]

    def __len__(self):
        return len(self.mutations)

    def __getitem__(self, idx):
        pos, aa = self.mutations[idx]
        mutated_sequence = self.seq[:pos] + aa + self.seq[pos + 1:]
        return pos, self.seq[pos], aa, mutated_sequence

def parse_arguments() -> Tuple[str, int, int]:
    """Parse command-line arguments to get the nanobody sequence, display limit, and batch size.

    Returns:
        Tuple[str, int, int]: The input nanobody sequence, number of top mutations to display, and batch size.
    """
    parser = argparse.ArgumentParser(description='Identify promising point mutations in a nanobody sequence using ESM log-likelihoods.')
    parser.add_argument('nanobody_sequence', type=str, help='The amino acid sequence of the nanobody in single-letter code.')
    parser.add_argument('--top-n', type=int, default=10, help='Number of top mutations to display (default: 10). Must be a positive integer.')
    parser.add_argument('--batch-size', type=int, default=16, help='Batch size for mutant log-likelihood calculations (default: 16). Must be a positive integer.')
    args = parser.parse_args()

    # Validate inputs
    if not all(aa in 'ACDEFGHIKLMNPQRSTVWY' for aa in args.nanobody_sequence):
        parser.error("Invalid sequence: Please ensure all characters are valid amino acid codes (A-Z).")
    if args.top_n <= 0:
        parser.error("Invalid --top-n value: Must be a positive integer.")
    if args.batch_size <= 0:
        parser.error("Invalid --batch-size value: Must be a positive integer.")

    return args.nanobody_sequence, args.top_n, args.batch_size

def compute_log_likelihood_ratios(seq: str, model, tokenizer, batch_size: int) -> List[Tuple[int, str, str, float]]:
    """Computes log-likelihood ratios for each possible point mutation in the sequence.

    Args:
        seq (str): The input nanobody sequence.
        model: The ESM model for masked language modeling.
        tokenizer: Tokenizer corresponding to the ESM model.
        batch_size (int): The batch size for processing mutations.

    Returns:
        List[Tuple[int, str, str, float]]: A list of tuples containing position, original amino acid, mutated amino acid, and log-likelihood ratio.
    """
    try:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model.to(device)
        model.eval()

        encoded_input = tokenizer(seq, return_tensors='pt', add_special_tokens=True).to(device)
        with torch.no_grad():
            original_output = model(**encoded_input)

        log_likelihoods = []
        amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
        dataset = MutationDataset(seq, amino_acids)
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False)

        for batch in tqdm(dataloader, desc="Calculating log-likelihoods"):
            positions, original_aas, mutated_aas, mutated_sequences = batch
            mutated_inputs = tokenizer(list(mutated_sequences), return_tensors='pt', padding=True, truncation=True, add_special_tokens=True).to(device)

            with torch.no_grad():
                mutated_outputs = model(**mutated_inputs)

            for i in range(len(positions)):
                pos = positions[i].item()
                original_aa = original_aas[i]
                mutated_aa = mutated_aas[i]

                original_ll = original_output.logits[0, pos + 1, tokenizer.convert_tokens_to_ids(original_aa)].item()
                mutated_ll = mutated_outputs.logits[i, pos + 1, tokenizer.convert_tokens_to_ids(mutated_aa)].item()
                ll_ratio = mutated_ll - original_ll

                log_likelihoods.append((pos + 1, original_aa, mutated_aa, ll_ratio))

        return sorted(log_likelihoods, key=lambda x: x[3], reverse=True)
    except Exception as e:
        print(f"An error occurred during computation: {e}. Please ensure your sequence is valid and model is correctly loaded.")
        return []

def main():
    nanobody_sequence, top_n, batch_size = parse_arguments()

    try:
        print("Loading model and tokenizer...")
        model = EsmForMaskedLM.from_pretrained('facebook/esm1b_t33_650M_UR50S')
        tokenizer = EsmTokenizer.from_pretrained('facebook/esm1b_t33_650M_UR50S')
    except Exception as e:
        print(f"Error loading model or tokenizer: {e}. Ensure you have installed 'transformers' and 'torch'.")
        print("Installation steps: pip install transformers torch")
        return

    if not torch.cuda.is_available():
        print("Warning: CUDA is not available. Running on CPU may be slow. Consider using a cloud service with GPU support.")
        print("For CUDA installation, visit: https://pytorch.org/get-started/locally/")

    print("Computing log-likelihood ratios...")
    mutations = compute_log_likelihood_ratios(nanobody_sequence, model, tokenizer, batch_size)

    if mutations:
        print(f"Top {top_n} suggested mutations (position, original_aa, mutated_aa, log_likelihood_ratio):")
        for mutation in mutations[:top_n]:
            print(mutation)
    else:
        print("No mutations could be computed. Please check your input sequence and model.")

    print("\nInterpretation:")
    print("Log-likelihood ratios indicate the relative likelihood of mutations improving binding affinity.")
    print("Higher positive values suggest potentially beneficial mutations, suitable for further experimental validation.")
    print("Consider the biological context, such as structural data or known functional regions, when prioritizing mutations for testing.")

if __name__ == '__main__':
    main()
