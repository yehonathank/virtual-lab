import torch
from esm import pretrained, Alphabet
import random
import numpy as np
from tqdm import trange


# Load the pretrained ESM model
def load_esm_model():
    """
    Load the pretrained ESM model and set it to evaluation mode.
    """
    model, alphabet = pretrained.esm1b_t33_650M_UR50S()
    model.eval()  # Disable dropout for evaluation
    model = model.cuda()
    return model, alphabet


# Function to set random seed for reproducibility
def set_seed(seed=42):
    random.seed(seed)
    torch.manual_seed(seed)


set_seed()


# Function to validate that the sequence only contains valid amino acid characters
def validate_sequence(seq):
    valid_amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    return all(char in valid_amino_acids for char in seq)


# Function to mutate a sequence by randomly substituting amino acids
def mutate_sequence(sequence, mutation_rate=0.01):
    """
    Mutate the given sequence at a specified mutation rate by randomly substituting amino acids.

    Parameters:
    sequence (str): The original antibody sequence.
    mutation_rate (float): The fraction of the sequence to mutate.

    Returns:
    str: The mutated sequence.
    """
    seq_len = len(sequence)
    num_mutations = int(seq_len * mutation_rate)
    mutated_sequence = list(sequence)

    valid_amino_acids = "ACDEFGHIKLMNPQRSTVWY"

    for _ in range(num_mutations):
        pos = np.random.randint(0, seq_len)
        orig_aa = sequence[pos]
        possible_subs = [aa for aa in valid_amino_acids if aa != orig_aa]

        new_aa = np.random.choice(possible_subs)
        mutated_sequence[pos] = new_aa

    return "".join(mutated_sequence)


# Function to calculate the log-likelihood ratio between wildtype and mutated sequences
def calculate_log_likelihood_ratio(model, alphabet, wildtype_seq, mutated_seqs):
    """
    Calculate the log-likelihood ratio between the wildtype and mutated sequences using the ESM model.

    Parameters:
    wildtype_seq (str): The original antibody sequence.
    mutated_seqs (list of str): The mutated antibody sequences.
    model (ESMModel): The ESM model instance.
    alphabet (ESMAlphabet): The ESM alphabet instance.

    Returns:
    list of float: The log-likelihood ratios.
    """
    batch_converter = alphabet.get_batch_converter()
    data = [("wildtype", wildtype_seq)] + [("mutant", seq) for seq in mutated_seqs]
    batch_labels, batch_strs, batch_tokens = batch_converter(data)
    batch_tokens = batch_tokens.cuda()

    with torch.no_grad():
        results = model(batch_tokens, repr_layers=[33])
        logits = results["logits"]

        log_probs_wt = torch.nn.functional.log_softmax(logits[0], dim=-1)
        log_probs_mut = torch.nn.functional.log_softmax(logits[1:], dim=-1)

        # Adjust sequence length to account for two additional tokens
        seq_len = len(wildtype_seq)
        wt_log_likelihood = log_probs_wt[
            torch.arange(1, seq_len + 1), batch_tokens[0, 1 : seq_len + 1]
        ].sum()

        mut_log_likelihoods = []
        for i in range(len(mutated_seqs)):
            mut_log_likelihood = log_probs_mut[
                i, torch.arange(1, seq_len + 1), batch_tokens[i + 1, 1 : seq_len + 1]
            ].sum()
            mut_log_likelihoods.append(mut_log_likelihood)

    log_likelihood_ratios = [
        mut_ll - wt_log_likelihood for mut_ll in mut_log_likelihoods
    ]
    return [llr.cpu().item() for llr in log_likelihood_ratios]


# Main function to run the mutation and evaluation process
def main():
    # Load the pretrained ESM model
    model, alphabet = load_esm_model()

    # Provided wild-type antibody sequence
    wildtype_seq = "QVQLVQSGAEVKKPGASVKVSCKASGYPFTSYGISWVRQAPGQGLEWMGWISTYNGNTNYAQKFQGRVTMTTDTSTTTGYMELRRLRSDDTAVYYCARDYTRGAWFGESLIGGFDNWGQGTLVTVSS"

    # Validate the original sequence
    if not validate_sequence(wildtype_seq):
        print("Invalid antibody sequence provided.")
        return

    # Generate multiple mutants
    num_mutants = 10000
    mutation_rate = 0.01
    mutants = [mutate_sequence(wildtype_seq, mutation_rate) for _ in range(num_mutants)]

    # Calculate log-likelihood ratios in batches
    batch_size = 100
    log_likelihood_ratios = []
    for i in trange(0, num_mutants, batch_size):
        batch_mutants = mutants[i : i + batch_size]
        batch_llrs = calculate_log_likelihood_ratio(
            model, alphabet, wildtype_seq, batch_mutants
        )
        log_likelihood_ratios.extend(batch_llrs)

    # Select top mutants by log-likelihood ratio
    top_indices = np.argsort(log_likelihood_ratios)
    top_mutants = [(mutants[i], log_likelihood_ratios[i]) for i in top_indices]

    # Output the results
    print(f"Wild-type sequence: {wildtype_seq}")
    for i, (mutant, llr) in enumerate(top_mutants, 1):
        mutations = [
            f"{wildtype_seq[pos]}{pos+1}{mutant[pos]}"
            for pos in range(len(wildtype_seq))
            if wildtype_seq[pos] != mutant[pos]
        ]
        print(f"Top {i} mutant: {mutant}")
        print(f"Mutations: {', '.join(mutations)}")
        print(f"Log-likelihood ratio: {llr}")


if __name__ == "__main__":
    main()
