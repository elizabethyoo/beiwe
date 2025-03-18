#!/bin/bash
#SBATCH -J one-hr_test
#SBATCH -c 1                      # Number of cores (-c)
#SBATCH -t 0-12:00:00                # Runtime in D-HH:MM, minimum of 10 minutes
#SBATCH -p sapphire,shared,intermediate,test,hsph,hsph_gpu                   # Submit to all partitions (wildcard for all partitions)
#SBATCH --mem=128G                # Memory pool for all cores (128GB total memory)
#SBATCH -o out_%j_download_data_passive.out          # File to which STDOUT will be written, %j inserts job ID
#SBATCH -e errors_%j_download_data_passive.err           # File to which STDERR will be written, %j inserts job ID
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=ecygraff@g.harvard.edu # email notification when job finishes 
echo "hello"
# Load modules
# for some reason fasrc doesn't have a 3.11.X version of python?
module load python/3.12.5-fasrc01
module load Mambaforge/23.11.0-fasrc01

/n/sw/Miniforge3-24.7.1-0/bin/python3 -m venv .venv
source .venv/bin/activate
pip install -r /n/home01/egraff/github/beiwe/code/forest_mano/slurm/requirements.txt

# TODO make path relative
# Run the python script with the same name as slurm in this script's parent folder
python /n/home01/egraff/github/beiwe/code/forest_mano/download_data_passive.py
