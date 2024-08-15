import sys
import argparse
from typing import List, Tuple, Dict
import torch
from esm import Alphabet, pretrained
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_args() -> argparse.Namespace:
    """
    Parses command-line arguments to get the input antibody sequence,
    probability threshold, model name, and number of top mutants to save.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Identify high-likelihood mutations in antibody sequences using ESM.")
    parser.add_argument("sequence", type=str, help="The antibody sequence to analyze (e.g., 'QVQLVQSGAEVKKPGASVKVSCKASGYTFTNYGMNWVRQAPGQGLEWMGWISYDGSTNYNPSLKSRLTITRDTSKNQFSLKLSSVTAADTAVYYC').")
    parser.add_argument("--threshold", type=float, default=0.05, help="Probability threshold for high-likelihood mutations (default: 0.05).")
    parser.add_argument("--model_name", type=str, default="esm1b_t33_650M_UR50S", help="The ESM model name to load (default: esm1b_t33_650M_UR50S).")
    parser.add_argument("--top_n", type=int, default=10, help="Number of top mutant sequences to save based on likelihood ratio (default: 10).")
    return parser.parse_args()

def load_esm_model(model_name: str) -> Tuple[torch.nn.Module, Alphabet]:
    """
    Loads the ESM model for predicting amino acid likelihoods.

    Args:
        model_name (str): The name of the pre-trained ESM model to load.

    Returns:
        model (torch.nn.Module): The loaded ESM model.
        alphabet (Alphabet): The model's alphabet for sequence encoding.

    Raises:
        RuntimeError: If the model fails to load.
    """
    try:
        model, alphabet = pretrained.load_model_and_alphabet(model_name)
        model.eval()  # Set the model to evaluation mode
        logging.info("Successfully loaded ESM model.")
        return model, alphabet
    except Exception as e:
        logging.error(f"Failed to load the ESM model {model_name}: {e}")
        raise RuntimeError(f"Failed to load the ESM model {model_name}: {e}")

def encode_sequence(sequence: str, alphabet: Alphabet) -> torch.Tensor:
    """
    Encodes the antibody sequence using the ESM model's alphabet.

    Args:
        sequence (str): The antibody sequence to encode.
        alphabet (Alphabet): The alphabet for encoding the sequence.

    Returns:
        torch.Tensor: The encoded sequence.

    Raises:
        ValueError: If the sequence contains invalid characters or is too short.
    """
    if not all(char in alphabet.standard_toks for char in sequence):
        raise ValueError("The sequence contains invalid characters.")

    if len(sequence) < 2:
        raise ValueError("The sequence is too short to be processed.")

    batch_converter = alphabet.get_batch_converter()
    data = [("antibody", sequence)]
    _, _, batch_tokens = batch_converter(data)
    return batch_tokens

def get_amino_acid_likelihoods(model: torch.nn.Module, tokens: torch.Tensor, alphabet: Alphabet) -> List[Tuple[int, str, float]]:
    """
    Gets the amino acid likelihoods for each position in the sequence.

    Args:
        model (torch.nn.Module): The ESM model.
        tokens (torch.Tensor): The encoded antibody sequence.
        alphabet (Alphabet): The model's alphabet.

    Returns:
        List[Tuple[int, str, float]]: A list of tuples containing the position, amino acid, and likelihood.
    """
    with torch.no_grad():
        logits = model(tokens, repr_layers=[33])["logits"].squeeze(0)

    probs = torch.nn.functional.softmax(logits, dim=-1)

    likelihoods = []
    for position in range(1, logits.size(0) - 1):  # Exclude start and end tokens
        aa_probs = probs[position]
        for idx, prob in enumerate(aa_probs):
            likelihoods.append((position, alphabet.all_toks[idx], prob.item()))
    return likelihoods

def identify_high_likelihood_mutations(sequence: str, likelihoods: List[Tuple[int, str, float]], threshold: float) -> List[Tuple[int, str, float, float]]:
    """
    Identifies high-likelihood mutations based on a probability threshold and ensures they are different from the wildtype.

    Args:
        sequence (str): The original antibody sequence.
        likelihoods (List[Tuple[int, str, float]]): A list of amino acid likelihoods.
        threshold (float): The probability threshold for identifying high-likelihood mutations.

    Returns:
        List[Tuple[int, str, float, float]]: A list of high-likelihood mutations (position, amino acid, likelihood, likelihood ratio).
    """
    high_likelihood_mutations = []
    wildtype_likelihoods = {pos: prob for pos, aa, prob in likelihoods if aa == sequence[pos - 1]}

    for pos, aa, prob in likelihoods:
        if prob >= threshold and aa != sequence[pos - 1] and aa in "ACDEFGHIKLMNPQRSTVWY":
            wildtype_prob = wildtype_likelihoods.get(pos)
            if wildtype_prob and prob > wildtype_prob:
                likelihood_ratio = prob / wildtype_prob
                high_likelihood_mutations.append((pos, aa, prob, likelihood_ratio))
    return high_likelihood_mutations

def main():
    """
    Main function to execute the prediction of high-likelihood amino acid mutations in an antibody sequence.
    This function integrates the steps of parsing input, loading the model, encoding the sequence,
    predicting likelihoods, identifying high-likelihood mutations, and outputting results.

    This script should be used as part of an iterative refinement process where the identified mutations
    can be fed into structural modeling or docking simulations for further validation and optimization.
    """
    # Parse command-line arguments
    args = parse_args()
    antibody_sequence = args.sequence
    threshold = args.threshold
    model_name = args.model_name
    top_n = args.top_n

    try:
        # Load the ESM model
        model, alphabet = load_esm_model(model_name)

        # Encode the antibody sequence
        tokens = encode_sequence(antibody_sequence, alphabet)

        # Get amino acid likelihoods
        likelihoods = get_amino_acid_likelihoods(model, tokens, alphabet)

        # Identify high-likelihood mutations
        high_likelihood_mutations = identify_high_likelihood_mutations(antibody_sequence, likelihoods, threshold)

        # Sort mutations by likelihood ratio and select top N
        high_likelihood_mutations.sort(key=lambda x: x[3], reverse=True)
        top_mutations = high_likelihood_mutations[:top_n]

        # Output the top high-likelihood mutations in JSON format
        output = {
            "sequence": antibody_sequence,
            "top_mutations": [
                {"position": pos, "amino_acid": aa, "likelihood": likelihood, "likelihood_ratio": ratio}
                for pos, aa, likelihood, ratio in top_mutations
            ]
        }
        print(json.dumps(output, indent=4))

    except ValueError as e:
        logging.error(f"Input error: {e}")
    except RuntimeError as e:
        logging.error(f"Runtime error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
