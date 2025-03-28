#!/bin/bash
#SBATCH --job-name=jas_24h	# Job name
#SBATCH --partition=fasse,fasse_bigmem,serial_requeue
#SBATCH --cpus-per-task=1		# Number of CPU cores per task
#SBATCH --mem=256GB				# Memory
#SBATCH --time=24:00:00			# Time limit hrs:min:sec
#SBATCH --array=40-43           # Batch size -- N jobs at a time
#SBATCH -o out_%j_jasmine.out          # File to which STDOUT will be written, %j inserts job ID
#SBATCH -e err_%j_jasmine.err           # File to which STDERR will be written, %j inserts job ID
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=ecygraff@g.harvard.edu # email notification when job finishes 

echo "Job Name: $SLURM_JOB_NAME, Task ID: $SLURM_ARRAY_TASK_ID, Job ID: $SLURM_JOB_ID"

source  /n/onnela_dp_l3/Lab/envs/.forest_venv/bin/activate

# python ../download.py $SLURM_ARRAY_TASK_ID
python ../0_jasmine_get_gps_daily.py $SLURM_ARRAY_TASK_ID
# python heatmap.py $SLURM_ARRAY_TASK_ID
# python oak.py $SLURM_ARRAY_TASK_ID

deactivate