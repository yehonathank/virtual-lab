import os
import subprocess
import csv
import argparse
from typing import List, Tuple
import concurrent.futures
import logging

def run_rosetta_script(pdb_file: str, xml_file: str, rosetta_executable: str, antibody_chain: str, antigen_chain: str) -> Tuple[str, float]:
    """
    Runs the RosettaScripts XML file on the provided PDB file and extracts the binding energy.

    :param pdb_file: Path to the PDB file.
    :param xml_file: Path to the RosettaScripts XML file.
    :param rosetta_executable: Path to the RosettaScripts executable.
    :param antibody_chain: Chain identifier for the antibody.
    :param antigen_chain: Chain identifier for the antigen.
    :return: Tuple containing the PDB filename and calculated binding energy.
    """
    cmd = [
        rosetta_executable,
        "-s", pdb_file,
        "-parser:protocol", xml_file,
        "-out:no_nstruct_label",
        "-parser:script_vars", f"antibody_chain={antibody_chain} antigen_chain={antigen_chain}"
    ]

    try:
        process = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Rosetta execution failed for {pdb_file}: {e}")
        return pdb_file, float('nan')

    # Parse the output to find the binding energy
    energy = None
    for line in process.stdout.splitlines():
        if "binding_energy" in line:
            energy = float(line.split()[-1])  # Assumes energy is the last column
            break

    if energy is None:
        logging.warning(f"Binding energy not found in output for {pdb_file}")
        return pdb_file, float('nan')

    return pdb_file, energy

def process_pdb_directory(directory: str, xml_file: str, rosetta_executable: str, output_csv: str, antibody_chain: str, antigen_chain: str) -> None:
    """
    Processes each PDB file in a directory to calculate binding energy and writes results to a CSV file.

    :param directory: Directory containing PDB files.
    :param xml_file: Path to the RosettaScripts XML file.
    :param rosetta_executable: Path to the RosettaScripts executable.
    :param output_csv: Path to the output CSV file.
    :param antibody_chain: Chain identifier for the antibody.
    :param antigen_chain: Chain identifier for the antigen.
    """
    pdb_files = [f for f in os.listdir(directory) if f.endswith('.pdb')]
    results = []

    # Use parallel processing for efficiency
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(run_rosetta_script, os.path.join(directory, pdb_file), xml_file, rosetta_executable, antibody_chain, antigen_chain)
            for pdb_file in pdb_files
        ]

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                results.append(result)
                logging.info(f"Processed {result[0]}: Binding energy = {result[1]}")
            except Exception as e:
                logging.error(f"Error processing a file: {e}")

    # Write results to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PDB File', 'Binding Energy'])
        writer.writerows(results)

    logging.info(f"Results saved to {output_csv}")

    # Basic statistical validation
    energies = [result[1] for result in results if not isinstance(result[1], float) or not result[1] == float('nan')]
    if energies:
        avg_energy = sum(energies) / len(energies)
        logging.info(f"Average binding energy: {avg_energy:.2f}")
        logging.info(f"Total structures processed: {len(results)}")
        logging.info(f"Structures with binding energy calculated: {len(energies)}")

def main():
    parser = argparse.ArgumentParser(description="Calculate binding energy of nanobody-antigen complexes.")
    parser.add_argument('--directory', required=True, help='Directory containing PDB files.')
    parser.add_argument('--xml_file', required=True, help='Path to the RosettaScripts XML file.')
    parser.add_argument('--rosetta_executable', required=True, help='Path to the RosettaScripts executable.')
    parser.add_argument('--output_csv', required=True, help='Path to the output CSV file.')
    parser.add_argument('--antibody_chain', required=True, help='Chain identifier for the antibody.')
    parser.add_argument('--antigen_chain', required=True, help='Chain identifier for the antigen.')
    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    process_pdb_directory(args.directory, args.xml_file, args.rosetta_executable, args.output_csv, args.antibody_chain, args.antigen_chain)

if __name__ == "__main__":
    main()
