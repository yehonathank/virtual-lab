# Nanobody Design

This README contains the commands needed to run the nanobody design workflow.


## Installation

After following the general `virtual_lab` installation instructions, run the following to install nanobody-specific requirements:

```bash
conda activate virtual_lab
pip install -r nanobody_design/requirements.txt
```

Additionally, create separate virtual environment for running AlphaFold-Multimer via LocalColabFold by following these instructions: https://github.com/YoshitakaMo/localcolabfold (or by running `install_localcolabfold.sh`). Make sure the following versions are installed:

```
alphafold-colabfold==2.3.6
colabfold==1.5.5
```


## LLM project design

Run the `run_nanobody_design.ipynb` notebook to have LLM agents create a nanobody-design workflow. The outputs of this notebook are the `nanobody_design/discussions` directory. The relevant ESM, AlphaFold-Multimer, and Rosetta scripts have been copied from those discussion to the `nanobody_design/scripts` folder. Additionally, the sequences for the relevant nanobodies selected by the LLM agents, along with SARS-CoV-2 spike RBD sequences, are in the `nanobody_design/sequences` directory.


## ESM

To run the ESM model, use the following command:

```bash
mkdir -p nanobody_design/designed/esm

for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
python nanobody_design/scripts/improved/esm.py \
    nanobody_design/sequences/nanobodies.csv \
    $NANOBODY \
    --output_csv nanobody_design/designed/esm/${NANOBODY}.csv
done
```


## ESM to AlphaFold-Multimer

To convert the ESM-designed mutated nanobody sequences to AlphaFold-Multimer nanobody-spike sequence inputs, use the following command:

```bash
for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
python nanobody_design/scripts/data_processing/esm_to_alphafold.py \
    --spike_sequences_path nanobody_design/sequences/spike.csv \
    --spike_name KP3 \
    --nanobody_sequences_path nanobody_design/designed/esm/${NANOBODY}.csv \
    --save_dir nanobody_design/designed/alphafold/sequences/${NANOBODY} \
    --top_n 10
done
````


## AlphaFold-Multimer

Run AlphaFold-Multimer on the nanobody-spike complexes.

```bash
for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
for FILE in nanobody_design/designed/alphafold/sequences/${NANOBODY}/*.fasta
do
NAME=$(basename "$FILE" .fasta)
colabfold_batch $FILE nanobody_design/designed/alphafold/structures/${NANOBODY}/$NAME
done
done
```

Process the AlphaFold-Multimer complexes to extract interface pLDDT scores:

```bash
for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
python nanobody_design/scripts/improved/alphafold.py \
    nanobody_design/designed/alphafold/structures/${NANOBODY} \
    B \
    A \
    nanobody_design/designed/alphafold/${NANOBODY}/scores.csv
done
```


## Rosetta

To run the Rosetta model, use the following command:

TODO: get Rosetta working

```bash
python nanobody_design/scripts/improved/rosetta.py
```

TODO: subsequent rounds
