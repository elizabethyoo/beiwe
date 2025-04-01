# Next, we can directly explore the structure of the sample Beiwe data that we've just downloaded. 

# At the top level of the directory `/data`, subject-level data is separately contained with subdirectories. Each subdirectory are named according to the subject's assigned Beiwe ID. In this sample, we observe the six subdirectories each from a separate study participant. 

def get_subdirectories(directory_path):
    """
    Returns a list of all subdirectory names in the specified directory.
    """
    # Check if the path exists and is a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"{directory_path} is not a valid directory")
    
    # Get all subdirectories
    subdirectories = [item for item in os.listdir(directory_path) 
                     if os.path.isdir(os.path.join(directory_path, item))]
    
    return subdirectories


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

# Task id from slurm job array arguments
task_id = int(sys.argv[1])
print("task_id: " + str(task_id), flush=True)

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



dest_dir = raw_data_folder

beiwe_id_df = pd.read_csv(metadata_path, sep = ",")

# convert patient id to string and then to list
beiwe_id_df["beiwe_id"] = beiwe_id_df["beiwe_id"].astype(str)
beiwe_ids = beiwe_id_df["beiwe_id"].tolist()
print(beiwe_ids)  

existing_beiwe_ids = get_subdirectories(raw_data_folder)
# intersecting beiwe ids between raw data (actually downloaded) and metadata (what should be downloaded)
shared_beiwe_ids = set(beiwe_ids) & set(existing_beiwe_ids)


# from forest.jasmine.traj2stats import gps_stats_main, Hyperparameters
# from forest.constants import Frequency

# user_params = pd.read_csv(metadata_path) # this is the file that contains the user parameters
# row = user_params.iloc[task_id]
# print(row)
# beiwe_ids = [row["beiwe_id"]]
# print("beiwe ids: " + str(beiwe_ids), flush=True)
gps_output_folder = "gps_output" # name of folder that will be created in data dir
gps_output_dir = os.path.abspath(os.path.join(data_dir, gps_output_folder))
print(f"gps output dir is: {gps_output_dir}", flush=True)

tz_str = "America/New_York"
freq = Frequency.HOURLY
save_traj = True 
# TEST ON SINGLE SUBJECT
beiwe_ids =  shared_beiwe_ids # shared_beiwe_ids # Test one id for now "d3o6kuvf" smallish dataset

places_of_interest = None
# if you are not interested in more specific hyperparameters, you can use the default ones
# by setting parameters = None or not passing in the parameters argument
parameters = Hyperparameters()
parameters.save_osm_log = False
parameters.log_threshold = 60 # threshold, in minutes, for logging locations if OSM analysis is enabled
parameters.pcr_bool = True # enables physical circadian rhythm (PCR) statistics
parameters.pcr_window = 14 # number of days to look back and forward for calculating PCR
parameters.pcr_sample_rate = 30 # sample rate in seconds

# print(f"Starting GPS download for one participant...", flush=True)
# beiwe_ids = ["aej6wxh8"] 
# gps_stats_main(
#     raw_data_folder, gps_output_dir, tz_str, freq, save_traj, places_of_interest=places_of_interest, 
#     participant_ids=beiwe_ids, parameters=parameters
# )
# print(f"Completed GPS download for {beiwe_ids}!", flush=True)


# Save the original pd.read_csv
_original_read_csv = pd.read_csv

def custom_read_csv(*args, **kwargs):
    # Set default to skip bad lines if not already specified
    kwargs.setdefault("on_bad_lines", "skip")
    return _original_read_csv(*args, **kwargs)

# Monkey patch pd.read_csv -- ignores problematic rows of raw gps data
pd.read_csv = custom_read_csv

# Now, when gps_stats_main is called, any internal call to pd.read_csv will use your custom version.
# gps_stats_main(
#     raw_data_folder, gps_output_dir, tz_str, freq, save_traj, 
#     places_of_interest=places_of_interest, participant_ids=[curr_beiwe_id], 
#     parameters=parameters
# )

beiwe_ids =  list(shared_beiwe_ids) # shared_beiwe_ids # Test one id for now "d3o6kuvf" smallish dataset
curr_beiwe_id = beiwe_ids[task_id]
print(f"Current beiwe id is: {curr_beiwe_id}", flush=True)
print(f"Starting GPS download...", flush=True)
print(f"starting download for participant {curr_beiwe_id}", flush=True)
gps_stats_main(
    raw_data_folder, gps_output_dir, tz_str, freq, save_traj, places_of_interest=places_of_interest, 
    participant_ids=[curr_beiwe_id], parameters=parameters
)
print(f"ending download for participant {curr_beiwe_id}", flush=True)
# undo monkey patch after processing gps raw data:
pd.read_csv = _original_read_csv


###############25-03-27 HERE ##################### 
# TODO: keep directory/path naming consistent
# from helper_functions import concatenate_summaries
# TODO: github issue with -- gps_stats_main for which I'm using monkey patch
    # problem id: ige4zl6o # task_id = 39
    
    
# print("Starting GPS summary concatenation..." , flush=True)
# concatenate_summaries(dir_path = os.path.join(data_dir, gps_output_dir), 
#                       output_filename = os.path.join(data_dir,"gps_summaries.csv"))

# print(f"GPS data processing complete. Output saved to {os.path.join(data_dir, 'gps_summaries.csv')}", flush=True)