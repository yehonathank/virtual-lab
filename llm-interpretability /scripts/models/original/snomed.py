import requests
import csv
import sys
import time
import logging
from typing import List, Dict, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.auth import HTTPBasicAuth

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration for SNOMED CT API
API_USERNAME = "your_username"  # Replace with your SNOMED CT API username
API_PASSWORD = "your_password"  # Replace with your SNOMED CT API password

def query_snomed_ct(concept: str, retries: int = 3) -> Tuple[str, str, float]:
    """
    Queries the SNOMED CT API to find the best matching concept for a given clinical term.
    
    :param concept: A string representing the clinical term to search for.
    :param retries: Number of times to retry the API request in case of failure.
    :return: A tuple containing the SNOMED CT concept ID, concept name, and confidence score.
    """
    url = f"https://browser.ihtsdotools.org/snowstorm/snomed-ct/v2/concepts?term={concept}&limit=10&active=true"
    
    for attempt in range(retries):
        try:
            response = requests.get(url, auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))
            response.raise_for_status()
            results = response.json().get('items', [])
            
            if not results:
                logging.warning(f"No results found for concept '{concept}'.")
                return ("", "", 0.0)
            
            # Improved ranking logic prioritizes fully defined and active concepts
            ranked_results = sorted(results, key=lambda x: (
                x.get('pt', {}).get('term', ''), 
                len(x.get('pt', {}).get('term', '')),
                x.get('definitionStatus', 'PRIMITIVE') == 'FULLY_DEFINED',
                x.get('active')
            ), reverse=True)

            best_match = ranked_results[0]
            snomed_id = best_match['conceptId']
            concept_name = best_match['pt']['term']
            confidence_score = 1.0 if best_match['active'] else 0.75
            
            return snomed_id, concept_name, confidence_score
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Error querying SNOMED CT API for concept '{concept}' (attempt {attempt + 1}): {e}")
            time.sleep(2 ** attempt)  # Exponential backoff

    return ("", "", 0.0)

def map_concepts_to_snomed(concepts: List[str]) -> List[Dict[str, str]]:
    """
    Maps a list of clinical terms to SNOMED CT concepts using the SNOMED CT API in parallel.
    
    :param concepts: A list of clinical terms.
    :return: A list of dictionaries containing the raw text, SNOMED ID, concept name, and confidence score.
    """
    mapped_concepts = []
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_concept = {executor.submit(query_snomed_ct, concept): concept for concept in concepts}
        for future in as_completed(future_to_concept):
            concept = future_to_concept[future]
            try:
                snomed_id, concept_name, confidence_score = future.result()
                mapped_concepts.append({
                    'raw_text': concept,
                    'snomed_id': snomed_id,
                    'concept_name': concept_name,
                    'confidence_score': confidence_score
                })
            except Exception as e:
                logging.error(f"Error processing concept '{concept}': {e}")
    
    return mapped_concepts

def save_to_csv(mapped_concepts: List[Dict[str, str]], filename: str) -> None:
    """
    Saves the mapped SNOMED CT concepts to a CSV file.
    
    :param mapped_concepts: A list of dictionaries containing the mapped concepts.
    :param filename: The filename for the output CSV file.
    """
    fieldnames = ['raw_text', 'snomed_id', 'concept_name', 'confidence_score']
    try:
        with open(filename, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for concept in mapped_concepts:
                writer.writerow(concept)
    except IOError as e:
        logging.error(f"Error saving data to {filename}: {e}")

def main():
    """
    Main function to parse input concepts from the command line, map them to SNOMED CT,
    and save the results to a CSV file.
    """
    if len(sys.argv) < 3:
        logging.error("Usage: python script.py <output_csv_filename> <concept1> <concept2> ... <conceptN>")
        sys.exit(1)
    
    filename = sys.argv[1]
    concepts = sys.argv[2:]
    
    # Input validation
    if not filename.endswith('.csv'):
        logging.error("Error: The output file must have a '.csv' extension.")
        sys.exit(1)
    
    mapped_concepts = map_concepts_to_snomed(concepts)
    save_to_csv(mapped_concepts, filename)
    logging.info(f"Results saved to {filename}")

if __name__ == "__main__":
    main()