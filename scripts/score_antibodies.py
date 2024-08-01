"""Script to score antibodies using ESM log-likelihood."""

from pathlib import Path

import pandas as pd
import torch
from esm import ESM2, Alphabet, BatchConverter, pretrained
from tqdm import trange


def load_esm_model() -> tuple[ESM2, Alphabet, BatchConverter]:
    """Load an ESM2 model and batch converter.

    :return: A tuple of a pretrained ESM2 model and a BatchConverter for preparing protein sequences as input.
    """
    model, alphabet = pretrained.esm2_t33_650M_UR50D()
    batch_converter = alphabet.get_batch_converter()
    model.eval()
    model = model.cuda()

    return model, alphabet, batch_converter


def esm_log_likelihood(
    wildtype_seq: str,
    mutant_seqs: list[str],
    batch_size: int = 128,
) -> list[float]:
    """Computes ESM log-likelihood ratio between wildtype and mutant sequences.

    :param wildtype_seq: The wildtype sequence.
    :param mutant_seqs: A list of mutant sequences.
    :param hub_dir: Path to directory where torch hub models are saved.
    :param batch_size: The batch size.
    :return: A list of log-likelihood ratios.
    """
    # Build sequences
    seqs = [wildtype_seq] + mutant_seqs
    seq_tuples = list(zip(seqs, seqs))

    # Load ESM2 model
    model, alphabet, batch_converter = load_esm_model()

    # Compute ESM2 log-likelihood ratios
    log_likelihood_ratios = []

    with torch.no_grad():
        # Iterate over batches of sequences
        for i in trange(0, len(seq_tuples), batch_size):
            # Get batch of sequences
            batch_protein_seq_tuples = seq_tuples[i : i + batch_size]
            batch_labels, batch_strs, batch_tokens = batch_converter(
                batch_protein_seq_tuples
            )
            batch_tokens = batch_tokens.cuda()

            # Compute logits
            results = model(batch_tokens, repr_layers=[33], return_contacts=False)
            logits = results["logits"]

            # Compute log probabilities
            log_probs_wt = torch.nn.functional.log_softmax(logits[0], dim=-1)
            log_probs_mut = torch.nn.functional.log_softmax(logits[1:], dim=-1)

            # Adjust sequence length to account for two additional tokens
            seq_len = len(wildtype_seq)
            wt_log_likelihood = log_probs_wt[
                torch.arange(1, seq_len + 1), batch_tokens[0, 1 : seq_len + 1]
            ].sum()

            mut_log_likelihoods = []
            for i in range(len(mutant_seqs)):
                mut_log_likelihood = log_probs_mut[
                    i,
                    torch.arange(1, seq_len + 1),
                    batch_tokens[i + 1, 1 : seq_len + 1],
                ].sum()
                mut_log_likelihoods.append(mut_log_likelihood)

        log_likelihood_ratios += [
            (mut_ll - wt_log_likelihood).cpu().item() for mut_ll in mut_log_likelihoods
        ]

    return log_likelihood_ratios


def create_mutant_seqs(
    wildtype_seq: str,
    mutants: list[str],
) -> list[str]:
    """Creates mutant sequences given wildtype sequence and mutations.

    :param wildtype_seq: The wildtype sequence.
    :param mutants: A list of mutations (e.g., P28T).
    :return: A list of mutant sequences.
    """
    # Create mutant sequences
    mutant_seqs = []
    for mutant in mutants:
        pos = int(mutant[1:-1]) - 1
        mutant_seq = wildtype_seq[:pos] + mutant[-1] + wildtype_seq[pos + 1 :]
        mutant_seqs.append(mutant_seq)

    return mutant_seqs


def score_antibodies(
    wildtype_seq: str,
    mutant_path: Path,
    mutant_column: str,
    save_path: Path,
    batch_size: int = 128,
) -> None:
    """Score antibodies using ESM log-likelihood.

    :param wildtype_seq: The wildtype sequence.
    :param mutant_path: Path to a CSV file containing mutations (of the form P28T).
    :param mutant_column: The column containing the mutations.
    :param save_path: Path to save the results.
    :param batch_size: The batch size.
    """
    # Load mutations
    mutant_seq_df = pd.read_csv(mutant_path)

    # Create mutant sequences
    mutant_seqs = create_mutant_seqs(
        wildtype_seq=wildtype_seq,
        mutants=mutant_seq_df[mutant_column],
    )

    # Score antibodies
    log_likelihood_ratios = esm_log_likelihood(
        wildtype_seq=wildtype_seq,
        mutant_seqs=mutant_seqs,
        batch_size=batch_size,
    )

    # Save results
    save_path.mkdir(parents=True, exist_ok=True)
    mutant_seq_df["log_likelihood_ratio"] = log_likelihood_ratios
    mutant_seq_df.to_csv(save_path, index=False)


if __name__ == "__main__":
    from tap import tapify

    tapify(score_antibodies)
