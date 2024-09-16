# Drug Discovery

This README contains the commands needed to run the drug discovery workflow.


## Installation

After following the general `virtual_lab` installation instructions, run the following to install drug discovery-specific requirements:

```bash
conda activate virtual_lab
pip install -r nanobody_design/requirements_drug_discovery.txt
```


## Emerald Cloud Labs documentation

Collect Emerald Cloud Labs (ECL) documentation for the agents to use. On September 15, 2024, text was copied and pasted from https://www.emeraldcloudlab.com/guides/runningexperiments?toggles=open to `drug_discovery/emerald/running_experiments.txt` and from https://www.emeraldcloudlab.com/guides/unitoperations?toggles=open to `drug_discovery/emerald/unit_operations.txt`. These files are then provided as context to the LLM agents when designing experiments with ECL. Additionally, once the LLM agents designed a workflow with specific ECL experiments in mind, text was copied and pasted (on September 16, 2024) from the relevant experiment page (e.g., [ExperimentPeptideSynthesis](https://www.emeraldcloudlab.com/helpfiles/experimentpeptidesynthesis)) to `drug_discovery/emerald/{experiment_name}.txt`. All text except for the "Warnings and Errors" section was copied.


## LLM project design

Run the `run_drug_discovery.ipynb` notebook to have LLM agents create a drug discovery workflow. The outputs of this notebook are the `drug_discovery/discussions` directory.
