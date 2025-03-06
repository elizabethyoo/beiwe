
# script to download certain passive data covariates from the HOPE dataset
# references
# forest_and_manu_usage.ipynb
# https://github.com/onnela-lab/als-beiwe-passive-data/blob/main/py/download_data_gps_AWS.py 
# TODO refactor to download all passive data covariates for all users in the HOPE study

# pasted from forest_and_mano_usage.ipynb; generalized to download for all participants in a given study
from platform import python_version
import sys

print(python_version()) ## Prints your version of python
print(sys.executable) ## Prints your current python installation

#run this chunk to install mano and forest
# requirements already satisfied -- commenting out
# pip install mano 
# pip install --upgrade https://github.com/onnela-lab/forest/tarball/develop
# pip install orjson

import os
# Test for one HOPE study, one user
# in the order of: DFCI_Wright_HOPE Trial Phase 2, DFCI_Wright_HOPE Trial Phase 2_Passive Data Only, DFCI_Wright_HOPE Trial, DFCI_Wright_HOPE Troubleshooting, DFCI_Wright_HOPE Test, DFCI_Wright_HOPE_Test 2
HOPE_STUDY_IDS = ['598365d5388cd66a62ac1f9e', '5a2ae1dc03d3c425ef0ea752', '588224eff4d48a76f488cdfd', '5a79f17d03d3c45080924ed4', '59c2b5b4388cd6715a958247', '5h7D9XT2vrN3BWkdcbYVNtpI'] 
study_id = HOPE_STUDY_IDS[0] # test on one part of the study 
direc = os.path.abspath("../../data/") # set to the desired directory
# to be used to pull participant ids
PART_TB_PATH = direc + "/trial_phase2_download_participants.csv"
# TODO change destination folder name to reflect the data being downloaded
dest_folder_name = "bulk_download_test_one_day" # TODO change to reflect the data being downloaded
server = "studies"
time_start = "2017-01-01"
time_end = "2017-01-02" # TODO for now test one day's to make sure data download script runs end to end
# for now focus on passive data - specifically gps and accelerometer
data_streams = ["gps", "accelerometer", "survey_timings", "survey_answers"] #, "survey_timings", "survey_answers", "audio_recordings", "calls", "texts", "accelerometer"]
# for now test on one user
# then pull all user ids from participant table 
import pandas as pd

# TODO: rename participant table with study id, rather than hardcoding 
beiwe_id_df = pd.read_csv(PART_TB_PATH, sep = ",")

# convert patient id to string and then to list
beiwe_id_df['Patient ID'] = beiwe_id_df['Patient ID'].astype(str)
beiwe_ids = beiwe_id_df['Patient ID'].tolist()
print(beiwe_ids) # sanity check 

# beiwe_ids = ['u2l3u6og'] 

dest_dir = os.path.join(direc, dest_folder_name)

# import .py file located in another directory if needed
import mano
sys.path.insert(0, direc)

import keyring_studies
kr = mano.keyring(None)


from helper_functions import download_data
download_data(kr, study_id, dest_dir, beiwe_ids, time_start, time_end, data_streams) 

# up until cell 5 in the forest_mano notebook ========================================
# TODO incorporate Marta(?)'s code to download all passive data covariates for all users in the HOPE study