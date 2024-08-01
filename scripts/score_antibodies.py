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
) -> list[float]:
    """Computes ESM log-likelihood ratio between wildtype and mutant sequences.

    :param wildtype_seq: The wildtype sequence.
    :param mutations: A list of mutations (e.g., P28T).
    :return: A list of log-likelihood ratios.
    """
    # Load ESM2 model
    model, alphabet, batch_converter = load_esm_model()

    # Get mutant positions and tokens
    mutant_pos = []
    mutant_tokens = []
    for mutant in mutations:
        mutant_pos.append(int(mutant[1:-1]) - 1)
        mutant_tokens.append(alphabet.tok_to_idx[mutant[-1]])

    mutant_pos = torch.tensor(mutant_pos).cuda()  # (num_mutants,)
    mutant_tokens = torch.tensor(mutant_tokens).cuda()  # (num_mutants,)

    # Prepare wildtype tokens
    _, _, batch_wildtype_tokens = batch_converter([("wildtype", wildtype_seq)])
    batch_wildtype_tokens = batch_wildtype_tokens.cuda()  # (1, seq_len + 2)

    # Get wildtype tokens that correspond to mutant tokens
    wildtype_tokens = batch_wildtype_tokens[0, 1 : len(wildtype_seq) + 1][
        mutant_pos
    ]  # (num_mutants,)

    # Compute wildtype log-likelihood
    with torch.no_grad():
        wildtype_logits = model(
            batch_wildtype_tokens, repr_layers=[33], return_contacts=False
        )[
            "logits"
        ]  # (1, seq_len + 2, vocab_size)

        wildtype_logits = wildtype_logits[
            0, 1 : len(wildtype_seq) + 1, :
        ]  # (seq_len, vocab_size)

    log_probs_wt = torch.nn.functional.log_softmax(
        wildtype_logits, dim=-1
    )  # (seq_len, vocab_size)

    # Compute log-likelihood ratios of mutants
    log_likelihood_ratios = (
        (
            log_probs_wt[mutant_pos, mutant_tokens]  # mutant log-likelihood
            - log_probs_wt[mutant_pos, wildtype_tokens]  # wildtype log-likelihood
        )
        .cpu()
        .tolist()
    )

    return log_likelihood_ratios


def score_antibodies(
    wildtype_seq: str,
    mutant_path: Path,
    mutant_column: str,
    save_path: Path,
) -> None:
    """Score antibodies using ESM log-likelihood.

    :param wildtype_seq: The wildtype sequence.
    :param mutant_path: Path to a CSV file containing mutations (of the form P28T).
    :param mutant_column: The column containing the mutations.
    :param save_path: Path to save the results.
    """
    # Load mutations
    mutant_seq_df = pd.read_csv(mutant_path)

    # Score antibodies
    log_likelihood_ratios = esm_log_likelihood(
        wildtype_seq=wildtype_seq,
        mutations=mutant_seq_df[mutant_column].tolist(),
    )

    # Save results
    save_path.parent.mkdir(parents=True, exist_ok=True)
    mutant_seq_df["log_likelihood_ratio"] = log_likelihood_ratios
    mutant_seq_df.to_csv(save_path, index=False)


if __name__ == "__main__":
    from tap import tapify

    tapify(score_antibodies)
