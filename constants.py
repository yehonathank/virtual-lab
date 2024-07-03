"""Holds constants."""

MODEL_TO_INPUT_PRICE_PER_TOKEN = {
    "gpt-3.5-turbo": 0.5 / 10**6,
    "gpt-4o": 5 / 10**6,
}

MODEL_TO_OUTPUT_PRICE_PER_TOKEN = {
    "gpt-3.5-turbo": 1.5 / 10**6,
    "gpt-4o": 15 / 10**6,
}
