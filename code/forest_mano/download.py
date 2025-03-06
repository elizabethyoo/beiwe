import os
import sys
import pandas as pd


HOPE_STUDY_IDS = ['598365d5388cd66a62ac1f9e', '5a2ae1dc03d3c425ef0ea752', '588224eff4d48a76f488cdfd',
                  '5a79f17d03d3c45080924ed4', '59c2b5b4388cd6715a958247', '5h7D9XT2vrN3BWkdcbYVNtpI']
study_id = HOPE_STUDY_IDS[0]  # test on one part of the study
direc = os.path.abspath("../../data/")  # set to the desired directory
# to be used to pull participant ids

# TODO change destination folder name to reflect the data being downloaded
# TODO change to reflect the data being downloaded

dest_folder_name = "bulk_download_test_one_day"
server = "studies"
time_start = "2017-01-01"
time_end = "2017-01-02"

task_id = int(sys.argv[1])
print("task_id: " + str(task_id))
METADATA_TB_PATH = os.path.join(direc, "trial_phase2_download_participants.csv")
user_params = pd.read_csv(METADATA_TB_PATH) # this is the file that contains the user parameters
row = user_params.iloc[task_id]
# row = user_params[user_params['index'] == task_id]

# study_id = row['study id'].values[0]
# direc = os.getcwd() #current working directory, 
# dest_folder_name = "raw_data"
# server = "studies"
# time_start = row['first_valid_date'].values[0]
# time_end = row['day_182'].values[0]
# cluster = row['cluster_label'].values[0]
# data_streams = ["gps", "survey_timings", "survey_answers", "audio_recordings", "calls", "texts", "accelerometer"]
# test gps for now -- change to include all passive features
data_streams = ["gps"] #, "survey_timings", "survey_answers", "audio_recordings", "calls", "texts", "accelerometer"]

beiwe_ids = [row['Patient ID'][0]]

# if dest_dir doesn't exist, create it

dest_dir = os.path.join(direc, dest_folder_name)
print("destination directory: " + dest_dir)

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)



import sys
import mano
sys.path.insert(0, '')

import keyring_studies
kr = mano.keyring(None)

from helper_functions import download_data

if pd.notna(cluster):
   download_data(kr, study_id, dest_dir, beiwe_ids, time_start, time_end, data_streams)

