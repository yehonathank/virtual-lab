# Virtual Lab

This repository contains code related to building a virtual lab with large language model (LLM) agents.


## Installation

Clone the repo, set up a conda environment, and install the required packages.

```bash
git clone https://github.com/swansonk14/virtual_lab.git
cd virtual_lab
conda create -y -n virtual_lab python=3.12
conda activate virtual_lab
pip install -e .
```


## Open AI API Key

Save the Open AI API key as the environment variable `OPENAI_API_KEY`. For example, add `export OPENAI_API_KEY=<your_key>` to your `.bashrc` or `.bash_profile`.


## Usage

To see examples of how to use the virtual lab, run the notebooks in the `nanobody_design/run_nanobody_design.ipynb` and `drug_discovery/run_drug_discovery.ipynb`.
