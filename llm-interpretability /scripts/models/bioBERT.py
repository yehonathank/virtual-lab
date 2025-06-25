import argparse
import json
import logging
import random
from typing import List, Dict, Any

import numpy as np
import torch
from transformers import BertTokenizer, BertForTokenClassification, Trainer, TrainingArguments
from transformers import DataCollatorForTokenClassification
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from datasets import load_dataset, Dataset
from lime.lime_text import LimeTextExplainer
import shap

# Set random seed for reproducibility
def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Preprocess input dataset to create token-level labels using Hugging Face Datasets
def preprocess_dataset(file_path: str, tokenizer: BertTokenizer, max_length: int) -> Dataset:
    logger.info(f"Loading dataset from {file_path}")
    dataset = load_dataset('csv', data_files=file_path)['train']

    def tokenize_and_align_labels(examples):
        tokenized_inputs = tokenizer(examples['text'], truncation=True, padding='max_length', max_length=max_length)
        labels = []
        for i, label in enumerate(examples['label']):
            word_ids = tokenized_inputs.word_ids(batch_index=i)
            label_ids = []
            previous_word_idx = None
            for word_idx in word_ids:
                if word_idx is None:
                    label_ids.append(-100)
                elif word_idx != previous_word_idx:
                    label_ids.append(label)
                else:
                    label_ids.append(-100)
                previous_word_idx = word_idx
            labels.append(label_ids)
        tokenized_inputs['labels'] = labels
        return tokenized_inputs

    tokenized_dataset = dataset.map(tokenize_and_align_labels, batched=True)
    return tokenized_dataset

# Function to compute evaluation metrics
def compute_metrics(pred) -> Dict[str, float]:
    labels = pred.label_ids.flatten()
    preds = pred.predictions.argmax(-1).flatten()
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='macro', zero_division=1)
    acc = accuracy_score(labels, preds)
    return {'accuracy': acc, 'f1': f1, 'precision': precision, 'recall': recall}

# Function to explain model predictions using LIME or SHAP
def explain_predictions(model, tokenizer, texts: List[str], max_length: int, method: str):
    explanations = []
    if method == 'LIME':
        explainer = LimeTextExplainer(class_names=["Class 0", "Class 1", "Class 2"])  # Adjust class names as needed
        for text in texts:
            exp = explainer.explain_instance(
                text, 
                lambda x: model(tokenizer(x, return_tensors='pt', truncation=True, padding=True, max_length=max_length).to(model.device))[0].detach().cpu().numpy(), 
                num_features=10, 
                num_samples=100
            )
            explanations.append(exp.as_list())
    elif method == 'SHAP':
        explainer = shap.Explainer(lambda x: model(tokenizer(x, return_tensors='pt', truncation=True, padding=True, max_length=max_length).to(model.device))[0].detach().cpu().numpy(), tokenizer)
        shap_values = explainer(texts)
        for sv in shap_values:
            explanations.append(sv.values)
    return explanations

# Main function to handle training and inference
def main(args):
    set_seed(42)

    tokenizer = BertTokenizer.from_pretrained(args.model_name)

    if not args.skip_training:
        # Load and preprocess the dataset
        dataset = preprocess_dataset(args.dataset_path, tokenizer, args.max_length)
        train_test_split = dataset.train_test_split(test_size=0.2, seed=42)
        train_dataset = train_test_split['train']
        test_dataset = train_test_split['test']

        # Fine-tune BioBERT/ClinicalBERT model for token classification
        logger.info(f"Loading model {args.model_name}")
        model = BertForTokenClassification.from_pretrained(args.model_name, num_labels=3)  # Adjust num_labels as needed

        training_args = TrainingArguments(
            output_dir='./results',
            num_train_epochs=args.epochs,
            per_device_train_batch_size=args.batch_size,
            per_device_eval_batch_size=args.batch_size,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir='./logs',
            evaluation_strategy="epoch",
            logging_steps=10,
            save_strategy="epoch"
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            compute_metrics=compute_metrics,
        )

        logger.info("Starting training")
        trainer.train()

        # Save the model and tokenizer
        model.save_pretrained('./model_checkpoint')
        tokenizer.save_pretrained('./model_checkpoint')

    else:
        # Load pre-finetuned model and tokenizer
        logger.info(f"Loading pre-finetuned model from {args.model_checkpoint}")
        model = BertForTokenClassification.from_pretrained(args.model_checkpoint)
        tokenizer = BertTokenizer.from_pretrained(args.model_checkpoint)

    logger.info("Starting inference")
    model.eval()
    data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)
    data_loader = torch.utils.data.DataLoader(test_dataset, batch_size=args.batch_size, collate_fn=data_collator)

    phenotype_results = {}

    for batch in data_loader:
        inputs = {k: v.to(trainer.args.device) for k, v in batch.items() if k != 'labels'}
        with torch.no_grad():
            outputs = model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=-1).cpu().numpy()

        for i, pred in enumerate(predictions):
            note_id = len(phenotype_results)
            tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][i])
            extracted_entities = [{
                "token": tokens[j],
                "position": j,
                "score": outputs.logits[i][j].max().item()  # Get the max logit score for the token
            } for j, p in enumerate(pred) if p != -100]

            phenotype_results[note_id] = {
                "text": test_dataset[i]['text'],
                "extracted_entities": extracted_entities
            }

    explanations = explain_predictions(model, tokenizer, [item['text'] for item in test_dataset], args.max_length, args.explanation_method)

    # Output the results to a JSON file
    output_data = {
        "phenotype_results": phenotype_results,
        "explanations": explanations
    }

    with open(args.output_file, 'w') as f:
        json.dump(output_data, f, indent=4)

    logger.info(f"Results saved to {args.output_file}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Fine-tune BioBERT/ClinicalBERT for phenotype extraction with interpretability")
    parser.add_argument('--dataset_path', type=str, required=True, help='Path to the primary dataset CSV file')
    parser.add_argument('--model_name', type=str, default='emilyalsentzer/Bio_ClinicalBERT', help='Pretrained model name')
    parser.add_argument('--max_length', type=int, default=128, help='Max sequence length for tokenization')
    parser.add_argument('--batch_size', type=int, default=8, help='Batch size for training and evaluation')
    parser.add_argument('--epochs', type=int, default=3, help='Number of training epochs')
    parser.add_argument('--output_file', type=str, default='phenotype_results.json', help='Output file for phenotype results')
    parser.add_argument('--skip_training', action='store_true', help='Skip training and only run inference')
    parser.add_argument('--model_checkpoint', type=str, help='Path to a pre-finetuned model checkpoint for inference')
    parser.add_argument('--explanation_method', type=str, choices=['LIME', 'SHAP'], default='LIME', help='Method for explaining predictions')
    args = parser.parse_args()

    main(args)