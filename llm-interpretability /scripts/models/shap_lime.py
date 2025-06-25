import argparse
import torch
import pandas as pd
import shap
import json
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from typing import List, Tuple
import matplotlib.pyplot as plt

def load_pipeline(model_name: str):
    """
    Load a transformers pipeline for sequence classification.

    :param model_name: The name of the model to load.
    :return: A transformers pipeline object.
    :raises RuntimeError: If there is an issue loading the model or pipeline.
    """
    try:
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return pipeline("text-classification", model=model, tokenizer=tokenizer)
    except Exception as e:
        raise RuntimeError(f"Error loading model or pipeline: {e}")

def compute_shap_values(pipeline, texts: List[str]) -> List[List[Tuple[str, float]]]:
    """
    Compute SHAP values for each token in the input texts.

    :param pipeline: The transformers pipeline for predictions.
    :param texts: A list of input texts to interpret.
    :return: A list of lists containing tuples of tokens and their SHAP values for each text.
    """
    explainer = shap.Explainer(pipeline, masker=shap.maskers.Text(pipeline.tokenizer))
    shap_values = explainer(texts)

    results = []
    for i, text in enumerate(texts):
        tokens = pipeline.tokenizer.convert_ids_to_tokens(shap_values.data[i])
        shap_vals = shap_values.values[i].mean(axis=1)
        # Remove special tokens
        filtered_tokens_and_values = [(token, value) for token, value in zip(tokens, shap_vals) if token not in ["[CLS]", "[SEP]"]]
        results.append(filtered_tokens_and_values)
    return results

def save_results(tokens_and_values: List[List[Tuple[str, float]]], output_file: str, format: str):
    """
    Save tokens and their corresponding SHAP values to a specified format.

    :param tokens_and_values: List of lists with tokens and their SHAP values.
    :param output_file: File path to save the results.
    :param format: The format to save the results in ('csv', 'json', 'html').
    """
    if format == 'csv':
        for i, tokens_values in enumerate(tokens_and_values):
            df = pd.DataFrame(tokens_values, columns=['Token', 'SHAP Value'])
            df.to_csv(f"{output_file}_{i}.csv", index=False)
    elif format == 'json':
        with open(output_file + '.json', 'w') as f:
            json.dump(tokens_and_values, f)
    elif format == 'html':
        for i, tokens_values in enumerate(tokens_and_values):
            shap.plots.text(tokens_values, show=False)
            plt.savefig(f"{output_file}_{i}.html")

def visualize_attributions(tokens_and_values: List[List[Tuple[str, float]]], plot_type: str):
    """
    Visualize token-level attribution using SHAP's built-in renderers.

    :param tokens_and_values: List of lists with tokens and their SHAP values.
    :param plot_type: The type of plot to generate ('bar', 'force', 'summary').
    """
    for tokens_values in tokens_and_values:
        tokens, shap_values = zip(*tokens_values)
        if plot_type == 'bar':
            plt.figure(figsize=(10, 2))
            plt.barh(range(len(tokens)), shap_values, color='b', align='center')
            plt.yticks(range(len(tokens)), tokens)
            plt.xlabel("SHAP Value")
            plt.title("Token-Level Attributions")
            plt.show()
        elif plot_type == 'force':
            shap.plots.force(shap_values)
        elif plot_type == 'summary':
            shap.plots.summary(shap_values)

def main():
    """
    Main function to handle command-line arguments and execute the SHAP interpretation.
    """
    parser = argparse.ArgumentParser(description='Interpret model outputs using SHAP for phenotype definitions.')
    parser.add_argument('--model_name', type=str, required=True, help='The name of the BioBERT/ClinicalBERT model.')
    parser.add_argument('--input_csv', type=str, required=True, help='Path to the CSV file containing input texts.')
    parser.add_argument('--output_file', type=str, required=True, help='Base path to save SHAP values.')
    parser.add_argument('--output_format', type=str, choices=['csv', 'json', 'html'], required=True, help='Output format for SHAP values.')
    parser.add_argument('--plot_type', type=str, choices=['bar', 'force', 'summary'], required=True, help='Type of plot to visualize SHAP values.')
    args = parser.parse_args()

    try:
        pipeline = load_pipeline(args.model_name)
        if not isinstance(pipeline.model, AutoModelForSequenceClassification):
            print("Warning: The loaded model may not be suitable for sequence classification.")
        
        df = pd.read_csv(args.input_csv)
        texts = df['text'].tolist()
        tokens_and_shap_values = compute_shap_values(pipeline, texts)
        save_results(tokens_and_shap_values, args.output_file, args.output_format)
        visualize_attributions(tokens_and_shap_values, args.plot_type)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()