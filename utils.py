"""Contains useful utility functions."""

import json
from pathlib import Path

import tiktoken

from constants import MODEL_TO_INPUT_PRICE_PER_TOKEN, MODEL_TO_OUTPUT_PRICE_PER_TOKEN


def count_tokens(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string.

    :param string: The text string to count tokens in.
    :param encoding_name: The name of the encoding to use.
    :return: The number of tokens in the text string.
    """
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))

    return num_tokens


def compute_token_cost(
    model: str, input_token_count: int, output_token_count: int
) -> float:
    """Computes the token cost of a model given input and output token counts.

    :param model: The name of the model.
    :param input_token_count: The number of tokens in the input.
    :param output_token_count: The number of tokens in the output.
    :return: The token cost of the model.
    """
    return (
        input_token_count * MODEL_TO_INPUT_PRICE_PER_TOKEN[model]
        + output_token_count * MODEL_TO_OUTPUT_PRICE_PER_TOKEN[model]
    )


def load_summaries(discussion_paths: list[Path]) -> tuple[str]:
    """Load summaries from a list of discussion paths.

    :param discussion_paths: The paths to the discussion JSON files. The summary is the last entry in the discussion.
    :return: A tuple of summaries.
    """
    summaries = []
    for discussion_path in discussion_paths:
        with open(discussion_path, "r") as file:
            discussion = json.load(file)
        summaries.append(discussion[-1]["content"])

    return tuple(summaries)
