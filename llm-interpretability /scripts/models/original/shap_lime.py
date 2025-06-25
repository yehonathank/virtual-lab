import argparse
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import shap
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Tuple

def load_model_and_tokenizer(model_name: str) -> Tuple[AutoTokenizer, AutoModelForSequenceClassification]:
    """
    Load a fine-tuned BioBERT/ClinicalBERT model and tokenizer.

    :param model_name: The name of the model to load from Hugging Face's model hub.
    :return: A tuple containing the tokenizer and model.
    :raises RuntimeError: If there is an issue loading the model or tokenizer.
    """
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        model.eval()
        return tokenizer, model
    except Exception as e:
        raise RuntimeError(f"Error loading model or tokenizer: {e}")

def compute_shap_values(model, tokenizer, text: str) -> List[Tuple[str, float]]:
    """
    Compute SHAP values for each token in the input text.

    :param model: The loaded transformer model.
    :param tokenizer: The tokenizer for the model.
    :param text: The input text to interpret.
    :return: A list of tuples containing tokens and their SHAP values.
    """
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    explainer = shap.Explainer(model, masker=shap.maskers.Text(tokenizer))
    shap_values = explainer(inputs)
    
    tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
    shap_values = shap_values.values[0].mean(axis=1)  # Aggregate SHAP values

    return list(zip(tokens, shap_values))

def save_to_csv(tokens_and_values: List[Tuple[str, float]], output_file: str):
    """
    Save tokens and their corresponding SHAP values to a CSV file.

    :param tokens_and_values: List of tuples with tokens and their SHAP values.
    :param output_file: File path to save the CSV.
    """
    df = pd.DataFrame(tokens_and_values, columns=['Token', 'SHAP Value'])
    df.to_csv(output_file, index=False)

def visualize_attributions(tokens_and_values: List[Tuple[str, float]]):
    """
    Visualize token-level attribution using matplotlib.

    :param tokens_and_values: List of tuples with tokens and their SHAP values.
    """
    tokens, shap_values = zip(*tokens_and_values)
    plt.figure(figsize=(10, 2))
    plt.barh(range(len(tokens)), shap_values, color='b', align='center')
    plt.yticks(range(len(tokens)), tokens)
    plt.xlabel("SHAP Value")
    plt.title("Token-Level Attributions")
    plt.show()

def main():
    """
    Main function to handle command-line arguments and execute the SHAP interpretation.
    """
    parser = argparse.ArgumentParser(description='Interpret model outputs using SHAP for phenotype definitions.')
    parser.add_argument('--model_name', type=str, required=True, help='The name of the BioBERT/ClinicalBERT model.')
    parser.add_argument('--input_text', type=str, required=True, help='The input text to analyze.')
    parser.add_argument('--output_csv', type=str, required=True, help='Path to save SHAP values in CSV format.')
    args = parser.parse_args()

    try:
        tokenizer, model = load_model_and_tokenizer(args.model_name)
        tokens_and_shap_values = compute_shap_values(model, tokenizer, args.input_text)
        save_to_csv(tokens_and_shap_values, args.output_csv)
        visualize_attributions(tokens_and_shap_values)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()