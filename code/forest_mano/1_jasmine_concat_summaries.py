# Next, we can directly explore the structure of the sample Beiwe data that we've just downloaded. 

# At the top level of the directory `/data`, subject-level data is separately contained with subdirectories. Each subdirectory are named according to the subject's assigned Beiwe ID. In this sample, we observe the six subdirectories each from a separate study participant. 


import os
from helper_functions import tree
from pathlib import Path
import pandas as pd
from forest.jasmine.traj2stats import gps_stats_main, Hyperparameters
from forest.constants import Frequency
import sys
import glob
import yaml
# TODO isolate get_subdirectories() to liz_helper_functions
# from liz_helper_functions import get_subdirectories
from tqdm import tqdm 
from helper_functions import concatenate_summaries




# Task id from slurm job array arguments
task_id = int(sys.argv[1])
print(f"[STDOUT] task_id: " + str(task_id), flush=True)

# Get the absolute path to the directory this script lives in
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # os.getcwd() for jupyter notebook

# Construct the path to the config file relative to the script
CONFIG_PATH = os.path.join(SCRIPT_DIR, "../../config/HOPE_config.yaml")
# # quick and dirty hardcoding for testing
# CONFIG_PATH = "/n/onnela_dp_l3/Lab/HOPE/beiwe/config/HOPE_config.yaml"
CONFIG_DIR = os.path.dirname(CONFIG_PATH)

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

# data_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["data_dir"]))
raw_data_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["raw_data_dir"]))
raw_data_folder = os.path.abspath(os.path.join(raw_data_dir, config["raw_data_folder"]))
metadata_path = os.path.abspath(os.path.join(CONFIG_DIR, config["metadata_path"]))

data_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["data_dir"]))

    
print(f"[STDOUT] Starting GPS summary concatenation..." , flush=True)
concatenate_summaries(dir_path = os.path.join(data_dir, gps_output_dir), 
                      output_filename = os.path.join(data_dir,"gps_summaries.csv"))

print(f"[STDOUT] GPS data processing complete. Output saved to {os.path.join(data_dir, 'gps_summaries.csv')}", flush=True)