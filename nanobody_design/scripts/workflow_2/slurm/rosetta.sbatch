#!/bin/bash
#
#SBATCH --job-name=rosetta
#
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --array=0-199
#SBATCH --partition=jamesz,owners
#SBATCH --output=/oak/stanford/groups/jamesz/swansonk/slurm/output/rosetta/%a.out
#SBATCH --error=/oak/stanford/groups/jamesz/swansonk/slurm/error/rosetta/%a.err
#SBATCH --time=4:00:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=swansonk@stanford.edu

echo "SLURM_JOBID=$SLURM_JOBID"
echo "SLURM_JOB_NAME=$SLURM_JOB_NAME"
echo "SLURM_JOB_NODELIST=$SLURM_JOB_NODELIST"
echo "SLURM_NNODES=$SLURM_NNODES"
echo "SLURMTMPDIR=$SLURMTMPDIR"
echo "working directory=$SLURM_SUBMIT_DIR"

source /home/users/swansonk/.bashrc

ml biology rosetta

cd /oak/stanford/groups/jamesz/swansonk/virtual_lab || exit

experiments=()

DIR_NAME="nanobody_design/designed/workflow_2"

ROUND_NUM=1

for NANOBODY in Nb21 Ty1
do
for SPIKE in KP.3 JN.1
do
for FILE in "${DIR_NAME}/round_${ROUND_NUM}/alphafold/structures/${SPIKE}/${NANOBODY}"/*/median_iplddt.pdb
do
NAME=$(basename "$(dirname "$FILE")")
experiment=""
for ITER in 1 2 3 4 5
do
OUTPUT_DIR="${DIR_NAME}/round_${ROUND_NUM}/rosetta/${SPIKE}/${NANOBODY}/${NAME}/${ITER}"
mkdir -p "${OUTPUT_DIR}"
experiment+="rosetta_scripts.default.linuxgccrelease \
    -s $FILE \
    -parser:protocol nanobody_design/scripts/workflow_2/models/rosetta.xml \
    -out:file:scorefile ${OUTPUT_DIR}/${NAME}.sc \
    -out:path:pdb ${OUTPUT_DIR}; "
done
experiments+=("${experiment}")
done
done
done

command=${experiments[SLURM_ARRAY_TASK_ID]}
echo "Task ID = $SLURM_ARRAY_TASK_ID"
echo "Number of experiments = ${#experiments[@]}"
echo "$command"
time (eval "$command")

echo "Done"
exit 0
