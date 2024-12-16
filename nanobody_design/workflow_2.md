## Nanobody design - workflow 2

Starting with two mutan nanobodies with experimentally validated binding to the JN.1 and/or KP.3 RBD of SARS-CoV-2---Nb21-I77V-L59E-Q87A-R37Q and Ty1-V32F-G59D-N54S-F32S---improve them by iteratively adding mutations and scoring them using ESM, AlphaFold-Multimer, and Rosetta for four rounds.


### ESM

For round 0, copy the mutated nanobodies and assign an ESM log-likelihood ratio of 0.

```bash
python -c "from pathlib import Path; import pandas as pd
for name in ['Nb21-I77V-L59E-Q87A-R37Q', 'Ty1-V32F-G59D-N54S-F32S']:
    nanobody = name.split('-')[0]
    data = pd.read_csv(f'nanobody_design/designed/workflow_1/combined/{nanobody}.csv')
    data = data[data['name'] == name]
    data = data[['sequence']]
    data['log_likelihood_ratio'] = 0.0
    save_dir = Path(f'nanobody_design/designed/workflow_2/round_0/esm/{nanobody}')
    save_dir.mkdir(parents=True, exist_ok=True)
    data.to_csv(save_dir / f'{name}.csv', index=False)"
```

For all subsequent rounds, run the ESM model.

```bash
ROUND_NUM=1
PREV_ROUND_NUM=$((ROUND_NUM - 1))

for NANOBODY in Nb21 Ty1
do
mkdir -p nanobody_design/designed/workflow_2/round_${ROUND_NUM}/esm/${NANOBODY}
python nanobody_design/scripts/workflow_2/models/esm.py \
    nanobody_design/designed/workflow_2/round_${PREV_ROUND_NUM}/scores/${NANOBODY}.csv \
    nanobody_design/designed/workflow_2/round_${ROUND_NUM}/esm/${NANOBODY}
done
```

Then, merge the ESM scores into a single file.

```bash
ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
python -c "from pathlib import Path;import pandas as pd
data = pd.concat([pd.read_csv(path).assign(name=path.stem) for path in Path('nanobody_design/designed/workflow_2/round_${ROUND_NUM}/esm/${NANOBODY}').glob('*.csv')])
data.to_csv('nanobody_design/designed/workflow_2/round_${ROUND_NUM}/esm/${NANOBODY}.csv', index=False)"
done
```

### ESM to AlphaFold-Multimer

Convert the top ESM-designed mutated nanobody sequences to AlphaFold-Multimer nanobody-spike sequence inputs.  (For round 0, add `--nanobody_sequence_col sequence`.)

```bash
ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
for SPIKE in KP.3 JN.1
do
python nanobody_design/scripts/workflow_2/data_processing/esm_to_alphafold.py \
    --spike_sequences_path nanobody_design/sequences/spike.csv \
    --spike_name ${SPIKE} \
    --nanobody_sequences_dir nanobody_design/designed/workflow_2/round_${ROUND_NUM}/esm/${NANOBODY} \
    --save_dir nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/sequences/${SPIKE}/${NANOBODY} \
    --top_n 50
done
done
```

### AlphaFold-Multimer

Run AlphaFold-Multimer on the nanobody-spike complexes.

```bash
ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
for SPIKE in KP.3 JN.1
do
for FILE in nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/sequences/${SPIKE}/${NANOBODY}/*.fasta
do
NAME=$(basename "$FILE" .fasta)
colabfold_batch $FILE nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/structures/${SPIKE}/${NANOBODY}/$NAME
done
done
done
```

Check that AlphaFold-Multimer ran correctly on all complexes.

```bash
ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
for SPIKE in KP.3 JN.1
do
python -c "from collections import Counter;from pathlib import Path
sequences = {path.stem for path in Path('nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/sequences/${SPIKE}/${NANOBODY}').glob('*.fasta')}
structures = Counter(path.parent.name for path in Path('nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/structures/${SPIKE}/${NANOBODY}').glob('**/*rank*.pdb'))

print(f'${NANOBODY} ${SPIKE}')
print(f'Number of sequences: {len(sequences):,}')
print(f'Number of structures: {len(structures):,}')

missing = [name for name in sequences if structures[name] != 5]
if missing:
    print(f'Sequences without all five structures: {\" \".join(missing)}')
print()"
done
done
```

Process the AlphaFold-Multimer complexes to extract interface pLDDT scores.

```bash
ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
for SPIKE in KP.3 JN.1
do
mkdir -p  nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/${SPIKE}
python nanobody_design/scripts/workflow_2/models/alphafold.py \
    nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/structures/${SPIKE}/${NANOBODY} \
    A \
    B \
    nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/${SPIKE}/${NANOBODY}.csv
done
done
```

### Rosetta

Run Rosetta to calculate interface binding energies.

```bash
ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
for SPIKE in KP.3 JN.1
do
for FILE in nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/structures/${SPIKE}/${NANOBODY}/*/median_iplddt.pdb
do
NAME=$(basename "$(dirname "$FILE")")
for ITER in 1 2 3 4 5
do
OUTPUT_DIR="nanobody_design/designed/workflow_2/round_${ROUND_NUM}/rosetta/${SPIKE}/${NANOBODY}/${NAME}/${ITER}"
mkdir -p "${OUTPUT_DIR}"
rosetta_scripts.default.linuxgccrelease \
    -s $FILE \
    -parser:protocol nanobody_design/scripts/workflow_2/models/rosetta.xml \
    -out:file:scorefile ${OUTPUT_DIR}/${NAME}.sc \
    -out:path:pdb ${OUTPUT_DIR}
done
done
done
done
```

Check that Rosetta ran correctly on all complexes.

```bash
ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
for SPIKE in KP.3 JN.1
do
python -c "from collections import Counter;from pathlib import Path
sequences = {path.stem for path in Path('nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold/sequences/${SPIKE}/${NANOBODY}').glob('*.fasta')}
structures = Counter(path.stem for path in Path('nanobody_design/designed/workflow_2/round_${ROUND_NUM}/rosetta/${SPIKE}/${NANOBODY}').glob('**/*.sc'))

print(f'${NANOBODY} ${SPIKE}')
print(f'Number of sequences: {len(sequences):,}')
print(f'Number of structures: {len(structures):,}')

missing = [name for name in sequences if structures[name] != 5]
if missing:
    print(f'Sequences without all five structures: {\" \".join(missing)}')
print()"
done
done
```

Then, collate the outputs.

```bash
ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
for SPIKE in KP.3 JN.1
do
python nanobody_design/scripts/workflow_2/models/rosetta.py \
    nanobody_design/designed/workflow_2/round_${ROUND_NUM}/rosetta/${SPIKE}/${NANOBODY} \
    nanobody_design/designed/workflow_2/round_${ROUND_NUM}/rosetta/${SPIKE}/${NANOBODY}.csv
done
done
```


### Combine scores

Combine scores from ESM, AlphaFold-Multimer, and Rosetta. (For round 0, add `--starting_sequence`.)

```bash
ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
python nanobody_design/scripts/workflow_2/data_processing/combine_scores.py \
    --esm_scores_dir nanobody_design/designed/workflow_2/round_${ROUND_NUM}/esm \
    --alphafold_scores_dir nanobody_design/designed/workflow_2/round_${ROUND_NUM}/alphafold \
    --rosetta_scores_dir nanobody_design/designed/workflow_2/round_${ROUND_NUM}/rosetta \
    --nanobody ${NANOBODY} \
    --spikes KP.3 JN.1 \
    --all_save_path nanobody_design/designed/workflow_2/round_${ROUND_NUM}/scores/${NANOBODY}_all.csv \
    --top_save_path nanobody_design/designed/workflow_2/round_${ROUND_NUM}/scores/${NANOBODY}.csv \
    --top_n 10 --starting_sequence
done
```

### Select nanobodies

After all the rounds have been run, select the best nanobodies.

```bash
for NANOBODY in Nb21 Ty1
do
python nanobody_design/scripts/workflow_2/data_processing/select_nanobodies.py \
    --score_path_pattern nanobody_design/designed/workflow_2/round_{round_num}/scores/${NANOBODY}_all.csv \
    --max_round 4 \
    --save_path nanobody_design/designed/workflow_2/selected/${NANOBODY}.csv \
    --top_n 24
done
```
