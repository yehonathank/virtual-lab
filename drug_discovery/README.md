# Drug Discovery

This README contains the commands needed to run the drug discovery workflow.


## Installation

After following the general `virtual_lab` installation instructions, run the following to install drug discovery-specific requirements:

```bash
conda activate virtual_lab
pip install -r nanobody_design/requirements_drug_discovery.txt
```


## Emerald Cloud Labs documentation

To provide the LLM agents with knowledge of the experiments and scientific instruments available at Emerald Cloud Labs (ECL), the ECL scientific instruments [page](https://www.emeraldcloudlab.com/instrumentation/) was downloaded on September 15, 2024, as a PDF. This PDF was uploaded to the ChatGPT [web interface](https://chatgpt.com/) (using GPT-4o) with the following prompt:

```
Please read the attached PDF and then write the name of every single experiment. After each experiment name, copy the example applications, if provided. For example, given this input text in quotes:

"ExperimentSolidPhaseExtraction(Beta)
Base Package

Example applications include: Compound Separation, Compound Purification, Mobile Phase, Solid Sorbent, Filtration

Small Robotic Liquid Handler
20 PSI pressure push (independent for each vessel)
0.1 to 100 mL/min flow rates for solvent pushes
Up to 20 L of wash solvent per batch
Up to 700 mL of equilibration buffer and elution buffer per batch
Filter through 3 cc or 6 cc SPE cartridges

Collects in SBS deep well plates

Positive Pressure Filter
0 to 40 PSI independent pressure sources for each well
Filter though SBS filter plates
Collects in SBS deep well plates"

You would then write the following text, provided here in quotes:

"ExperimentSolidPhaseExtraction(Beta)

Example applications include: Compound Separation, Compound Purification, Mobile Phase, Solid Sorbent, Filtration"

Write down every single experiment except for those listed in the sections titled "Under Development" or "Future Roadmap".
```

TODO: get this working


## LLM project design

Run the `run_drug_discovery.ipynb` notebook to have LLM agents create a drug discovery workflow. The outputs of this notebook are the `drug_discovery/discussions` directory.
