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


## Nanobody design

Design improved nanobodies by iteratively adding mutations and scoring them using ESM, AlphaFold-Multimer, and Rosetta.

### ESM

For round 0, copy the original nanobodies and assign an ESM log-likelihood ratio of 0.

```bash
for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
python -c "from pathlib import Path; import pandas as pd
data = pd.read_csv('nanobody_design/sequences/nanobodies.csv')
data = data[data['name'] == '${NANOBODY}']
data['log_likelihood_ratio'] = 0.0
save_dir = Path('nanobody_design/designed/round_0/esm/${NANOBODY}')
save_dir.mkdir(parents=True, exist_ok=True)
data.to_csv(save_dir / '${NANOBODY}.csv', index=False)"
done
```

For all subsequent rounds, run the ESM model.

```bash
ROUND_NUM=1

mkdir -p nanobody_design/designed/round_${ROUND_NUM}/esm

for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
python nanobody_design/scripts/improved/esm.py \
    nanobody_design/designed/round_${ROUND_NUM-1}/scores/${NANOBODY}.csv \
    --save_dir nanobody_design/designed/round_${ROUND_NUM}/esm/${NANOBODY} \
    --top_n 20
done
```


### ESM to AlphaFold-Multimer

Convert the ESM-designed mutated nanobody sequences to AlphaFold-Multimer nanobody-spike sequence inputs. (For round 0, add `--nanobody_sequence_col sequence`.)

```bash
ROUND_NUM=1

for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
python nanobody_design/scripts/data_processing/esm_to_alphafold.py \
    --spike_sequences_path nanobody_design/sequences/spike.csv \
    --spike_name KP3 \
    --nanobody_sequences_dir nanobody_design/designed/round_${ROUND_NUM}/esm/${NANOBODY} \
    --save_dir nanobody_design/designed/round_${ROUND_NUM}/alphafold/sequences/${NANOBODY} \
    --top_n 20
done
```


### AlphaFold-Multimer

Run AlphaFold-Multimer on the nanobody-spike complexes.

```bash
ROUND_NUM=1

for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
for FILE in nanobody_design/designed/round_${ROUND_NUM}/alphafold/sequences/${NANOBODY}/*.fasta
do
NAME=$(basename "$FILE" .fasta)
colabfold_batch $FILE nanobody_design/designed/round_${ROUND_NUM}/alphafold/structures/${NANOBODY}/$NAME
done
done
```

Process the AlphaFold-Multimer complexes to extract interface pLDDT scores.

```bash
ROUND_NUM=1

for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
python nanobody_design/scripts/improved/alphafold.py \
    nanobody_design/designed/round_${ROUND_NUM}/alphafold/structures/${NANOBODY} \
    A \
    B \
    nanobody_design/designed/round_${ROUND_NUM}/alphafold/${NANOBODY}.csv
done
```


### Rosetta

Run Rosetta to calculate interface binding energies.

```bash
ROUND_NUM=1

for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
OUTPUT_DIR="nanobody_design/designed/round_${ROUND_NUM}/rosetta/${NANOBODY}"
mkdir -p "${OUTPUT_DIR}"

for FILE in nanobody_design/designed/round_${ROUND_NUM}/alphafold/structures/${NANOBODY}/*/*unrelaxed_rank_001*.pdb
do
NAME=$(basename "$(dirname "$FILE")")
rosetta_scripts.default.linuxgccrelease \
    -s $FILE \
    -parser:protocol nanobody_design/scripts/improved/rosetta.xml \
    -out:file:scorefile ${OUTPUT_DIR}/${NAME}.sc \
    -out:path:pdb ${OUTPUT_DIR}
done
done
```

Then, collate the outputs with the following command:

```bash
ROUND_NUM=1

for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
python nanobody_design/scripts/improved/rosetta.py \
    nanobody_design/designed/round_${ROUND_NUM}/rosetta/${NANOBODY} \
    nanobody_design/designed/round_${ROUND_NUM}/rosetta/${NANOBODY}.csv
done
```


### Combine scores

Combine scores from ESM, AlphaFold-Multimer, and Rosetta:

```bash
ROUND_NUM=1

for NANOBODY in Ty1 H11-D4 Nb21 VHH-72
do
python nanobody_design/scripts/data_processing/combine_scores.py \
    --esm_scores_path nanobody_design/designed/round_${ROUND_NUM}/esm/${NANOBODY}.csv \
    --alphafold_scores_path nanobody_design/designed/round_${ROUND_NUM}/alphafold/${NANOBODY}.csv \
    --rosetta_scores_path nanobody_design/designed/round_${ROUND_NUM}/rosetta/${NANOBODY}.csv \
    --save_path nanobody_design/designed/round_${ROUND_NUM}/scores/${NANOBODY}.csv \
    --top_n 5
done
```

## Round 2

Repeat the above steps but with the top selected mutant nanobodies from the previous round.

Ty1: Ty1-V32A Ty1-P45L Ty1-V32D Ty1-V32Y Ty1-V32T

H11-D4: H11-D4-K74N H11-D4-R45L H11-D4-R27Y H11-D4-R27I H11-D4-R27S

Nb21: Nb21-R43P Nb21-R43M Nb21-R37Q Nb21-Q87G Nb21-Q87D

VHH-72: VHH-72-R27C VHH-72-F37V VHH-72-D89E VHH-72-R27F VHH-72-R27Y

TODO: subsequent rounds
