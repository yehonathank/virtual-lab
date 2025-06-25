#!/bin/bash

# Step 1: Run BioBERT training & inference (adjust args as needed)
python biobert.py --dataset_path ./data/dataset.csv --output_file ./output/phenotype_results.json --skip_training

# Check if phenotype_results.json was created
if [ ! -f ./output/phenotype_results.json ]; then
  echo "Error: phenotype_results.json not found!"
  exit 1
fi

# Step 2: Run SNOMED mapping
# Example: Provide output filename and concepts as command line args
python snomed.py ./output/snomed_mappings.json shortest_term diabetes hypertension asthma

# Check if snomed_mappings.json was created
if [ ! -f ./output/snomed_mappings.json ]; then
  echo "Error: snomed_mappings.json not found!"
  exit 1
fi

# Step 3: Combine results into visualization CSV
python combine_results.py ./output/phenotype_results.json ./output/snomed_mappings.json ./output/visualization_ready.csv

if [ ! -f ./output/visualization_ready.csv ]; then
  echo "Error: visualization_ready.csv not found!"
  exit 1
fi

# Step 4: Run Dash app with combined CSV
echo "Launching Dash app with visualization_ready.csv..."
python app.py --data-file ./output/visualization_ready.csv
