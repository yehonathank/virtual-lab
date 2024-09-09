# Nanobody Design

This README contains the commands needed to run the nanobody design workflow.

## Installation

First, install the general `virtual_lab` requirements:

```bash
pip install -r requirements.txt
```

Then, install the `nanobody_design` requirements:

```bash
pip install -r nanobody_design/requirements.txt
```

## ESM

To run the ESM model, use the following command:

```bash
python nanobody_design/scripts/improved/esm.py
```

## AlphaFold-Multimer

To run the AlphaFold-Multimer model, use the following command:

```bash
python nanobody_design/scripts/improved/alphafold_multimer.py
```

## Rosetta

To run the Rosetta model, use the following command:

```bash
python nanobody_design/scripts/improved/rosetta.py
```
