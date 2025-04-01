#!/bin/bash
#SBATCH --job-name=download	# Job name
#SBATCH --partition=fasse,fasse_bigmem,fasse_ultramem,serial_requeue,test
#SBATCH --cpus-per-task=1		# Number of CPU cores per task
#SBATCH --mem=512GB				# Memory
#SBATCH --time=12:00:00			# Time limit hrs:min:sec
#SBATCH --array=19
#SBATCH -o out_%j_download.out          # File to which STDOUT will be written, %j inserts job ID
#SBATCH -e err_%j_download.err           # File to which STDERR will be written, %j inserts job ID
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=ecygraff@g.harvard.edu # email notification when job finishes 

echo "Job Name: $SLURM_JOB_NAME, Task ID: $SLURM_ARRAY_TASK_ID, Job ID: $SLURM_JOB_ID"

source  /n/onnela_dp_l3/Lab/envs/.forest_venv/bin/activate

python ../0_auto_download.py $SLURM_ARRAY_TASK_ID


deactivate