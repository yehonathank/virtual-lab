import argparse
import json
import logging
import random
import pandas as pd
from typing import List, Dict, Any

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertForTokenClassification, Trainer, TrainingArguments
from transformers import DataCollatorForTokenClassification
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from lime.lime_text import LimeTextExplainer

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

# Define a dataset class for token classification
class ClinicalNotesTokenDataset(Dataset):
    """Dataset for clinical notes with token-level labels."""
    def __init__(self, texts: List[str], labels: List[List[int]], tokenizer: BertTokenizer, max_length: int):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self) -> int:
        return len(self.texts)

    def __getitem__(self, idx: int):
        encoding = self.tokenizer(
            self.texts[idx],
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        labels = self.labels[idx] + [0] * (self.max_length - len(self.labels[idx]))
        item = {key: val.squeeze(0) for key, val in encoding.items()}
        item['labels'] = torch.tensor(labels, dtype=torch.long)
        return item

# Preprocess input dataset to create token-level labels
def preprocess_dataset(file_path: str, additional_dataset_path: str = None) -> Dict[str, List]:
    logger.info(f"Loading dataset from {file_path}")
    df = pd.read_csv(file_path)
    if not {'text', 'label'}.issubset(df.columns):
        raise ValueError("Dataset must contain 'text' and 'label' columns.")

    df = df.dropna(subset=['text', 'label'])

    if additional_dataset_path:
        logger.info(f"Loading additional dataset from {additional_dataset_path} for few-shot learning")
        additional_df = pd.read_csv(additional_dataset_path)
        additional_df = additional_df.dropna(subset=['text', 'label'])
        df = pd.concat([df, additional_df], ignore_index=True)

    # Convert document-level labels to token-level labels
    def create_token_labels(text, label):
        return [int(label)] * len(text.split())

    df['token_labels'] = df.apply(lambda row: create_token_labels(row['text'], row['label']), axis=1)

    train_texts, test_texts, train_labels, test_labels = train_test_split(
        df['text'].tolist(), df['token_labels'].tolist(), test_size=0.2, random_state=42
    )

    return {
        'train_texts': train_texts,
        'train_labels': train_labels,
        'test_texts': test_texts,
        'test_labels': test_labels
    }

# Function to compute evaluation metrics
def compute_metrics(pred) -> Dict[str, float]:
    labels = pred.label_ids.flatten()
    preds = pred.predictions.argmax(-1).flatten()
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='binary', zero_division=1)
    acc = accuracy_score(labels, preds)
    return {'accuracy': acc, 'f1': f1, 'precision': precision, 'recall': recall}

# Function to explain model predictions using LIME
def explain_predictions(model, tokenizer, texts: List[str], max_length: int):
    explainer = LimeTextExplainer(class_names=["Not Relevant", "Relevant"])
    explanations = []
    for text in texts:
        exp = explainer.explain_instance(text, lambda x: model(tokenizer(x, return_tensors='pt', truncation=True, padding=True, max_length=max_length).to(model.device))[0].detach().cpu().numpy(), num_features=10, num_samples=100)
        explanations.append(exp.as_list())
    return explanations

# Main function to handle training and inference
def main(args):
    set_seed(42)

    # Load and preprocess the dataset
    data = preprocess_dataset(args.dataset_path, args.additional_dataset_path)

    tokenizer = BertTokenizer.from_pretrained(args.model_name)
    train_dataset = ClinicalNotesTokenDataset(data['train_texts'], data['train_labels'], tokenizer, args.max_length)
    test_dataset = ClinicalNotesTokenDataset(data['test_texts'], data['test_labels'], tokenizer, args.max_length)

    # Fine-tune BioBERT/ClinicalBERT model for token classification
    logger.info(f"Loading model {args.model_name}")
    model = BertForTokenClassification.from_pretrained(args.model_name, num_labels=2)

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

    logger.info("Starting inference")
    model.eval()
    data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)
    data_loader = DataLoader(test_dataset, batch_size=args.batch_size, collate_fn=data_collator)

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
            } for j, p in enumerate(pred) if p == 1]

            phenotype_results[note_id] = {
                "text": data['test_texts'][i],
                "extracted_entities": extracted_entities
            }

    explanations = explain_predictions(model, tokenizer, data['test_texts'], args.max_length)

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
    parser.add_argument('--additional_dataset_path', type=str, help='Path to an additional dataset CSV file for few-shot learning')
    parser.add_argument('--model_name', type=str, default='emilyalsentzer/Bio_ClinicalBERT', help='Pretrained model name')
    parser.add_argument('--max_length', type=int, default=128, help='Max sequence length for tokenization')
    parser.add_argument('--batch_size', type=int, default=8, help='Batch size for training and evaluation')
    parser.add_argument('--epochs', type=int, default=3, help='Number of training epochs')
    parser.add_argument('--output_file', type=str, default='phenotype_results.json', help='Output file for phenotype results')
    args = parser.parse_args()

    main(args)