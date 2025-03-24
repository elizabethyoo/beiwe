import os
import sys
import pandas as pd


HOPE_STUDY_IDS = ['598365d5388cd66a62ac1f9e', '5a2ae1dc03d3c425ef0ea752', '588224eff4d48a76f488cdfd',
                  '5a79f17d03d3c45080924ed4', '59c2b5b4388cd6715a958247', '5h7D9XT2vrN3BWkdcbYVNtpI']
study_id = HOPE_STUDY_IDS[0]  # test on one part of the study

## TODO merge all download_participant metadata with HOPE_2_study_demographics data
## name it demographics_info = "../data/HOPE_paper2_demographics_w_beiwe_metadata.csv"
## 2025-03-24 TODO import variables from demographics_info in configs


# Get the absolute path of the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
direc = os.path.abspath(os.path.join(script_dir, "../../data/"))  # set to the desired directory
print(f"Resolved absolute path: {direc}")

# to be used to pull participant ids

# TODO change destination folder name to reflect the data being downloaded
# TODO change to reflect the data being downloaded

dest_folder_name = "bulk_download_test"
server = "studies"

task_id = int(sys.argv[1])
print("task_id: " + str(task_id))
METADATA_TB_PATH = os.path.join(direc, "trial_phase2_download_participants.csv")
print(METADATA_TB_PATH)

user_params = pd.read_csv(METADATA_TB_PATH) # this is the file that contains the user parameters
row = user_params.iloc[task_id]
print(row)

# study_id = row['study id'].values[0]
# direc = os.getcwd() #current working directory, 
# dest_folder_name = "raw_data"

server = "studies"

time_start = row['First Registration Date'].split(" ")[0]
print("First Registration Date: " + str(time_start))
time_end = None

# data_streams = ["gps", "survey_timings", "survey_answers", "audio_recordings", "calls", "texts", "accelerometer"]
# test gps for now -- change to include all passive features
data_streams = ["gps", "accelerometer", "survey_timings", "survey_answers"] #, "survey_timings", "survey_answers", "audio_recordings", "calls", "texts", "accelerometer"]
print("requested features: " + str(data_streams))

beiwe_ids = [row['Patient ID']]
print("beiwe_ids: " + str(beiwe_ids))

# if dest_dir doesn't exist, create it
dest_dir = os.path.join(direc, dest_folder_name)
print("destination directory: " + dest_dir)

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

print("starting download for task_id: " + str(task_id))
download_data(kr, study_id, dest_dir, beiwe_ids, time_start, time_end, data_streams)
print("completed download for task_id: " + str(task_id))

