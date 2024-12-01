import os
import pandas as pd
import argparse
import logging
from glob import glob


def extract_scores_from_file(score_file: str) -> float:
    """
    Extract the dG_separated score from a Rosetta score file.

    Parameters:
    score_file (str): Path to the score file.

    Returns:
    float: The extracted dG_separated score.
    """
    try:
        with open(score_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("SCORE:") and "dG_separated" in line:
                    columns = line.split()
                    # Find the index of the dG_separated column
                    dg_separated_index = columns.index("dG_separated")
                elif line.startswith("SCORE:") and not line.startswith(
                    "SCORE: total_score"
                ):
                    values = line.split()
                    return float(values[dg_separated_index])
        raise ValueError(f"No valid dG_separated score found in {score_file}")
    except Exception as e:
        logging.error(f"Error processing file {score_file}: {e}")
        return None


def main(input_dir: str, output_csv: str) -> None:
    """
    Process multiple Rosetta score files and output a CSV with average scores per subdirectory.

    Parameters:
    input_dir (str): Directory containing subdirectories with score files.
    output_csv (str): Output CSV file path.
    """
    logging.basicConfig(level=logging.INFO)
    subdirectories = [
        os.path.join(input_dir, d)
        for d in os.listdir(input_dir)
        if os.path.isdir(os.path.join(input_dir, d))
    ]
    averages = []
    errors = []

    for subdir in subdirectories:
        score_files = glob(os.path.join(subdir, "**/*.sc"), recursive=True)
        scores = []
        for score_file in score_files:
            score = extract_scores_from_file(score_file)
            if score is not None:
                scores.append(score)
            else:
                errors.append(os.path.basename(score_file))

        if scores:
            average_score = sum(scores) / len(scores)
            averages.append((os.path.basename(subdir), average_score))

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(averages, columns=["Subdirectory", "Average dG_separated"])
    df.to_csv(output_csv, index=False)

    # Log errors if any
    if errors:
        logging.warning(
            "Encountered errors in the following files; these files may have invalid or missing data:"
        )
        for error_file in errors:
            logging.warning(f" - {error_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process Rosetta score files and output CSV."
    )
    parser.add_argument(
        "input_dir",
        type=str,
        help="Directory containing subdirectories with Rosetta score files.",
    )
    parser.add_argument("output_csv", type=str, help="Output CSV file path.")
    args = parser.parse_args()

    main(args.input_dir, args.output_csv)
