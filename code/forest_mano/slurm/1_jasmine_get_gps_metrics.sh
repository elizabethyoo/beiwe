#!/bin/bash
#SBATCH --job-name=jas # Job name
#SBATCH --partition=fasse,fasse_bigmem,fasse_ultramem,serial_requeue,test
#SBATCH --cpus-per-task=1		# Number of CPU cores per task
#SBATCH --mem=512GB				# Memory
#SBATCH --time=12:00:00			# Time limit hrs:min:sec

#SBATCH -o out_%A_%a_jas.out          # File to which STDOUT will be written, %j inserts job ID
#SBATCH -e err_%A_%a_jas.err           # File to which STDERR will be written, %j inserts job ID
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=ecygraff@g.harvard.edu # email notification when job finishes 

echo "Job Name: $SLURM_JOB_NAME, Task ID: $SLURM_ARRAY_TASK_ID, Job ID: $SLURM_JOB_ID"

source  /n/onnela_dp_l3/Lab/envs/.forest_venv/bin/activate

python ../1_jasmine_get_gps_metrics.py $SLURM_ARRAY_TASK_ID


deactivate