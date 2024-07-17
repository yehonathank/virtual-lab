# Virtual Lab

This repository contains code related to building a virtual lab with large language model agents.

## Installation

Clone the repo, set up a conda environment, and install the required packages.

```bash
git clone https://github.com/swansonk14/virtual_lab.git
cd virtual_lab
conda create -y -n virtual_lab python=3.12
conda activate virtual_lab
pip install -r requirements.txt
```

## Open AI API Key

Save the Open AI API key as the environment variable `OPENAI_API_KEY`.

## Usage

Run one of the notebooks, either `run_antibody_design.ipynb` or `run_drug_discovery.ipynb`.
