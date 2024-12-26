#!/bin/bash
#
#SBATCH --job-name=alphafold_missing
#
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gpus=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --array=0-1%15
#SBATCH --partition=jamesz,owners
#SBATCH --output=/oak/stanford/groups/jamesz/swansonk/slurm/output/alphafold_missing/%a.out
#SBATCH --error=/oak/stanford/groups/jamesz/swansonk/slurm/error/alphafold_missing/%a.err
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

conda activate localcolabfold

cd /oak/stanford/groups/jamesz/swansonk/virtual_lab || exit

experiments=()

DIR_NAME="nanobody_design/designed/workflow_2"

ROUND_NUM=1

for EXP in Ty1-V32F-G59D-N54S-F32S-T7S-N101S_JN.1 Ty1-V32F-G59D-N54S-F32S-L102S-I58T_JN.1
do
NANOBODY=$(echo "$EXP" | cut -d'-' -f1)
SPIKE=$(echo "$EXP" | cut -d'_' -f2)
FILE="${DIR_NAME}/round_${ROUND_NUM}/alphafold/sequences/${SPIKE}/${NANOBODY}/${EXP}.fasta"
NAME=$(basename "$FILE" .fasta)
OUT_DIR="${DIR_NAME}/round_${ROUND_NUM}/alphafold/structures/${SPIKE}/${NANOBODY}/$NAME"
if [ -d "$OUT_DIR" ]; then
rm -r "$OUT_DIR"
fi
experiments+=("colabfold_batch $FILE $OUT_DIR")
done

command=${experiments[SLURM_ARRAY_TASK_ID]}
echo "Task ID = $SLURM_ARRAY_TASK_ID"
echo "Number of experiments = ${#experiments[@]}"
echo "$command"
time (eval "$command")

echo "Done"
exit 0
