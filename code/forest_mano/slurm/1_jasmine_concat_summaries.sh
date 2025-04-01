#!/bin/bash
#SBATCH --job-name=jasconcat # Job name
#SBATCH --partition=fasse,fasse_bigmem,fasse_ultramem,serial_requeue,test
#SBATCH --cpus-per-task=1		# Number of CPU cores per task
#SBATCH --mem=512GB				# Memory
#SBATCH --time=12:00:00			# Time limit hrs:min:sec

#SBATCH -o out_%j_jasconcat.out          # File to which STDOUT will be written, %j inserts job ID
#SBATCH -e err_%j_jasconcat.err           # File to which STDERR will be written, %j inserts job ID
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=ecygraff@g.harvard.edu # email notification when job finishes 

echo "Job Name: $SLURM_JOB_NAME, Task ID: $SLURM_ARRAY_TASK_ID, Job ID: $SLURM_JOB_ID"

source  /n/onnela_dp_l3/Lab/envs/.forest_venv/bin/activate

python ../1_jasmine_concat_summaries.py $SLURM_ARRAY_TASK_ID > out_%j_jasconcat.out  2> err_%j_jasconcat.err


deactivate