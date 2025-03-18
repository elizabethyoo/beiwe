#!/bin/bash
#SBATCH --job-name=5_download_test		# Job name
#SBATCH --cpus-per-task=1		# Number of CPU cores per task
#SBATCH --mem=15GB				# Memory
#SBATCH --time=25:00:00			# Time limit hrs:min:sec
#SBATCH --array=1-5
#SBATCH -o out_%j_download.out          # File to which STDOUT will be written, %j inserts job ID
#SBATCH -e err_%j_download.err           # File to which STDERR will be written, %j inserts job ID
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=ecygraff@g.harvard.edu # email notification when job finishes 
echo "hello"

source  ~/python_envs/forest_env/bin/activate

python ../download.py $SLURM_ARRAY_TASK_ID
# python heatmap.py $SLURM_ARRAY_TASK_ID
# python oak.py $SLURM_ARRAY_TASK_ID


deactivate