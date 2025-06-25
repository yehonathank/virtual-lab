import json
import csv

def create_visualization_csv(
    phenotype_results_path: str,
    snomed_mappings_path: str,
    output_csv_path: str
) -> None:
    """
    Combines phenotype extraction results and SNOMED mappings into a CSV
    for visualization with the Plotly Dash app.

    :param phenotype_results_path: Path to phenotype_results.json
    :param snomed_mappings_path: Path to snomed_mappings.json
    :param output_csv_path: Path to output CSV file
    """
    # Load phenotype results
    with open(phenotype_results_path, 'r') as f:
        phenotype_data = json.load(f)

    # Load SNOMED mappings
    with open(snomed_mappings_path, 'r') as f:
        snomed_data = json.load(f)

    # Build a term lookup from SNOMED mappings
    snomed_lookup = {entry['raw_text'].lower(): entry for entry in snomed_data}

    # Prepare rows
    rows = []
    for patient_id, info in phenotype_data['phenotype_results'].items():
        tokens = [ent['token'] for ent in info['extracted_entities']]
        shap_values = [ent['score'] for ent in info['extracted_entities']]
        predicted_phenotypes = info.get('predicted_phenotypes', [])  # Optional
        text = info['text'].lower()

        # Match SNOMED terms if any of them appear in the raw text
        matched_terms = []
        for raw_text, mapping in snomed_lookup.items():
            if raw_text in text:
                matched_terms.append(f"{mapping['concept_name']} ({mapping['snomed_id']})")

        row = {
            'patient_id': patient_id,
            'tokens': ','.join(tokens),
            'shap_values': ','.join(map(str, shap_values)),
            'predicted_phenotypes': '; '.join(predicted_phenotypes) if predicted_phenotypes else '',
            'matched_snomed_terms': '; '.join(matched_terms)
        }
        rows.append(row)

    # Write to CSV
    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV saved to {output_csv_path}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print("Usage: python combine_results.py <phenotype_results.json> <snomed_mappings.json> <output_csv>")
        sys.exit(1)
    create_visualization_csv(sys.argv[1], sys.argv[2], sys.argv[3])