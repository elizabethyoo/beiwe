# Next, we can directly explore the structure of the sample Beiwe data that we've just downloaded. 

# At the top level of the directory `/data`, subject-level data is separately contained with subdirectories. Each subdirectory are named according to the subject's assigned Beiwe ID. In this sample, we observe the six subdirectories each from a separate study participant. 
import os
from helper_functions import tree
from pathlib import Path
import pandas as pd
from forest.jasmine.traj2stats import gps_stats_main, Hyperparameters
from forest.constants import Frequency


# Get the absolute path of the script directory -- CHANGE AS NECESSARY 
script_dir = os.path.dirname(os.path.abspath(__file__))
direc = os.path.abspath(os.path.join(script_dir, "../../data/"))  # set to the desired directory
print(f"Resolved absolute path: {direc}")
dest_folder_name = "bulk_download_test"
# if dest_dir doesn't exist, create it
dest_dir = os.path.join(direc, dest_folder_name)
print("destination directory: " + dest_dir)
PART_TB_PATH = direc + "/download_participants/trial_phase2_download_participants.csv"

# TODO: rename participant table with study id, rather than hardcoding 
beiwe_id_df = pd.read_csv(PART_TB_PATH, sep = ",")

# convert patient id to string and then to list
beiwe_id_df['Patient ID'] = beiwe_id_df['Patient ID'].astype(str)
beiwe_ids = beiwe_id_df['Patient ID'].tolist()
print(beiwe_ids)  

tree(dest_dir, level=1, limit_to_directories=True)

from forest.jasmine.traj2stats import gps_stats_main, Hyperparameters
from forest.constants import Frequency

data_dir = dest_dir
gps_output_dir = "gps_output"
tz_str = "America/New_York"
freq = Frequency.DAILY
save_traj = True 
beiwe_ids = ["2n18iikg"] # Test one id for now "2n18iikg"
places_of_interest = None

# if you are not interested in more specific hyperparameters, you can use the default ones
# by setting parameters = None or not passing in the parameters argument
parameters = Hyperparameters()
parameters.save_osm_log = False
parameters.log_threshold = 60 # threshold, in minutes, for logging locations if OSM analysis is enabled
parameters.pcr_bool = True # enables physical circadian rhythm (PCR) statistics
parameters.pcr_window = 14 # number of days to look back and forward for calculating PCR
parameters.pcr_sample_rate = 30 # sample rate in seconds

gps_stats_main(
    data_dir, gps_output_dir, tz_str, freq, save_traj, places_of_interest = places_of_interest, 
    participant_ids = beiwe_ids, parameters = parameters
)

from helper_functions import concatenate_summaries


concatenate_summaries(dir_path = os.path.join(direc, gps_output_dir), 
                      output_filename = os.path.join(direc,"gps_summaries.csv"))

print(f"GPS data processing complete. Output saved to {os.path.join(direc, 'gps_summaries.csv')}")