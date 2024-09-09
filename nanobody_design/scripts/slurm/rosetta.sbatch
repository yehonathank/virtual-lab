#!/bin/bash
#
#SBATCH --job-name=rosetta
#
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --array=0
#SBATCH --partition=jamesz,sfgf,owners
#SBATCH --output=/oak/stanford/groups/jamesz/swansonk/slurm/output/rosetta/%a.out
#SBATCH --error=/oak/stanford/groups/jamesz/swansonk/slurm/error/rosetta/%a.err
#SBATCH --time=2:00:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=swansonk@stanford.edu

echo "SLURM_JOBID="$SLURM_JOBID
echo "SLURM_JOB_NAME="$SLURM_JOB_NAME
echo "SLURM_JOB_NODELIST"=$SLURM_JOB_NODELIST
echo "SLURM_NNODES"=$SLURM_NNODES
echo "SLURMTMPDIR="$SLURMTMPDIR
echo "working directory="$SLURM_SUBMIT_DIR

source /home/users/swansonk/.bashrc

ml biology rosetta

cd /oak/stanford/groups/jamesz/swansonk/virtual_lab || exit

ID="8K3K"
CHAINS="D_E"

experiments=("mkdir ${ID}_relax;
relax.default.linuxgccrelease -s ${ID}.pdb -nstruct 1 -relax:fast -out:path:all ${ID}_relax;
mkdir ${ID}_interface;
InterfaceAnalyzer.default.linuxgccrelease -s ${ID}_relax/${ID}_0001.pdb -interface ${CHAINS} -pack_input 1 -pack_separated 1 -out:path:all ${ID}_interface")

command=${experiments[SLURM_ARRAY_TASK_ID]}
echo "Task ID = $SLURM_ARRAY_TASK_ID"
echo "Number of experiments = ${#experiments[@]}"
echo $command
time (eval "$command")

echo "Done"
exit 0
