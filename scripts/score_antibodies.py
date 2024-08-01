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
    mutations: list[str],
    batch_size: int = 128,
) -> list[float]:
    """Computes ESM log-likelihood ratio between wildtype and mutant sequences.

    :param wildtype_seq: The wildtype sequence.
    :param mutations: A list of mutations (e.g., P28T).
    :param batch_size: The batch size.
    :return: A list of log-likelihood ratios.
    """
    # Load ESM2 model
    model, alphabet, batch_converter = load_esm_model()

    # Create mutant sequences
    mutant_seqs = []
    mutant_pos = []
    for mutant in mutations:
        pos = int(mutant[1:-1]) - 1
        mutant_seq = wildtype_seq[:pos] + mutant[-1] + wildtype_seq[pos + 1 :]
        mutant_seqs.append(mutant_seq)
        mutant_pos.append(pos)

    mutant_pos = torch.tensor(mutant_pos)

    # Get sequence length
    seq_len = len(wildtype_seq)
    assert all(len(seq) == seq_len for seq in mutant_seqs)

    # Compute wildtype log-likelihood
    _, _, wildtype_tokens = batch_converter([("wildtype", wildtype_seq)])
    wildtype_tokens = wildtype_tokens.cuda()

    wildtype_logits = model(wildtype_tokens, repr_layers=[33], return_contacts=False)[
        "logits"
    ]

    log_probs_wt = torch.nn.functional.log_softmax(wildtype_logits[0], dim=-1)

    # Compute ESM2 log-likelihood ratios of mutants
    log_likelihood_ratios = []

    with torch.no_grad():
        # Iterate over batches of mutant sequences
        for i in trange(0, len(mutant_seqs), batch_size):
            # Get batch of sequences
            batch_mut_pos = mutant_pos[i : i + batch_size].cuda()
            _, _, batch_tokens = batch_converter(
                [("mutant", seq) for seq in mutant_seqs[i : i + batch_size]]
            )
            batch_tokens = batch_tokens.cuda()

            # Compute logits
            logits = model(batch_tokens, repr_layers=[33], return_contacts=False)[
                "logits"
            ]

            # Compute log probabilities
            log_probs_mut = torch.nn.functional.log_softmax(logits, dim=-1)

            # Compute log-likelihood ratios
            seq_indices = torch.arange(batch_tokens.shape[0])
            batch_mut_tokens = batch_tokens[seq_indices, batch_mut_pos]
            batch_log_likelihood_ratios = (
                log_probs_mut[seq_indices, batch_mut_pos, batch_mut_tokens]
                - log_probs_wt[batch_mut_pos, batch_mut_tokens]
            )
            log_likelihood_ratios += batch_log_likelihood_ratios.cpu().tolist()

    return log_likelihood_ratios


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

    # Score antibodies
    log_likelihood_ratios = esm_log_likelihood(
        wildtype_seq=wildtype_seq,
        mutations=mutant_seq_df[mutant_column].tolist(),
        batch_size=batch_size,
    )

    # Save results
    save_path.parent.mkdir(parents=True, exist_ok=True)
    mutant_seq_df["log_likelihood_ratio"] = log_likelihood_ratios
    mutant_seq_df.to_csv(save_path, index=False)


if __name__ == "__main__":
    from tap import tapify

    tapify(score_antibodies)
