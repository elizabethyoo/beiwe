import sys
import os
import yaml
import pandas as pd
from forest.oak.base import run
from forest.constants import Frequency


# Get the absolute path to the directory this script lives in
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # os.getcwd() for jupyter notebook os.path.dirname(os.path.abspath(__file__)) for script

# Construct the path to the config file relative to the script
CONFIG_PATH = os.path.join(SCRIPT_DIR, "../../config/HOPE_config.yaml")
# # quick and dirty hardcoding for testing
# CONFIG_PATH = "/n/onnela_dp_l3/Lab/HOPE/beiwe/config/HOPE_config.yaml"
CONFIG_DIR = os.path.dirname(CONFIG_PATH)
# import hardcoded variables e.g., study name to ID mappings, directory paths, etc. from config file


with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)
# dload_part_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["download_participants_dir"]))
# data_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["data_dir"]))
# raw_data_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["raw_data_dir"]))
# raw_data_path = os.path.abspath(os.path.join(CONFIG_DIR, config["raw_data_folder"])) 
# metadata_path = os.path.abspath(os.path.join(CONFIG_DIR, config["metadata_path"]))
raw_data_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["raw_data_dir"]))
raw_data_path = os.path.abspath(os.path.join(raw_data_dir, config["raw_data_folder"]))
metadata_path = os.path.abspath(os.path.join(CONFIG_DIR, config["metadata_path"]))

data_dir = os.path.abspath(os.path.join(CONFIG_DIR, config["data_dir"]))
acc_output_folder = "acc_output" # name of folder that will be created in data dir
acc_output_dir = os.path.abspath(os.path.join(data_dir, acc_output_folder))

# task_id = int(sys.argv[1])
# # task_id = 0 

# beiwe_id_df = pd.read_csv(metadata_path)
# row = beiwe_id_df.iloc[task_id]


# tz_str = "America/New_York"
# frequency = Frequency.HOURLY_AND_DAILY

# beiwe_ids = [row['beiwe_id']]
# # cluster = row['cluster_label'].values[0]

# run(raw_data_path, acc_output_dir, tz_str, frequency, users = beiwe_ids)

from helper_functions import concatenate_summaries

direc = data_dir
FREQUENCY = "hourly" # or "daily"
accelerometer_output_dir = os.path.abspath(os.path.join(data_dir, acc_output_folder, FREQUENCY))
print(f"accelerometer_output_dir: {accelerometer_output_dir}", flush=True)

concatenate_summaries(dir_path = os.path.join(direc, accelerometer_output_dir), 
                      output_filename = os.path.join(direc,"accel_summaries.csv"))