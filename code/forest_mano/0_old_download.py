import os
import sys
import glob
import pandas as pd
import yaml

# Get the absolute path to the directory this script lives in
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the config file relative to the script
CONFIG_PATH = os.path.join(SCRIPT_DIR, "../../config/HOPE_config.yaml")
# # quick and dirty hardcoding for testing
# CONFIG_PATH = "/n/onnela_dp_l3/Lab/HOPE/beiwe/config/HOPE_config.yaml"
CONFIG_DIR = os.path.dirname(CONFIG_PATH)

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

data_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["data_dir"]))
raw_data_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["raw_data_dir"]))
metadata_path = os.path.abspath(os.path.join(CONFIG_DIR, config["metadata_path"]))


# set the download destination directory
direc = raw_data_dir
print(f"Resolved absolute path: {direc}", flush=True)

dest_folder_name = "HOPE_paper2_download"
server = "studies"

task_id = int(sys.argv[1])
print("task_id: " + str(task_id), flush=True)

user_params = pd.read_csv(metadata_path) # this is the file that contains the user parameters
row = user_params.iloc[task_id]
print(row)

study_id = row["study_id"]
server = "studies"

time_start = row["first_registration_date"].split(" ")[0]
print("first registration date: " + str(time_start), flush=True)
time_end = None

# data_streams = ["gps", "survey_timings", "survey_answers", "audio_recordings", "calls", "texts", "accelerometer"]
# test gps for now -- change to include all passive features
data_streams = ["gps", "accelerometer", "survey_timings", "survey_answers"] #, "survey_timings", "survey_answers", "audio_recordings", "calls", "texts", "accelerometer"]
print("requested features: " + str(data_streams), flush=True)

# user_params = pd.read_csv(metadata_path) # this is the file that contains the user parameters
# row = user_params.iloc[task_id]
# print(row)
beiwe_ids = [row["beiwe_id"]]
print("beiwe ids: " + str(beiwe_ids), flush=True)

# if dest_dir doesn't exist, create it
dest_dir = os.path.join(direc, dest_folder_name)
print("destination directory: " + dest_dir, flush=True)
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
    
# import .py file located in another directory if needed
import mano
import sys
sys.path.insert(0, direc)

import keyring_studies
kr = mano.keyring(None)

import os

from helper_functions import download_data

print("starting download for task_id: " + str(task_id), flush=True)
download_data(kr, study_id, dest_dir, beiwe_ids, time_start, time_end, data_streams)
print("completed download for task_id: " + str(task_id), flush=True)
