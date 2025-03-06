import sys
import pandas as pd
from forest.oak.base import run
from forest.constants import Frequency

task_id = int(sys.argv[1])
user_params = pd.read_csv("final_participant_data_with_clusters.csv")
row = user_params[user_params['index'] == task_id]

data_dir = "raw_data"
accelerometer_output_dir = "accel_output"
tz_str = "America/New_York"
frequency = Frequency.MINUTE
beiwe_ids = [row['participant id'].values[0]]
cluster = row['cluster_label'].values[0]

if pd.notna(cluster):
   run(data_dir, accelerometer_output_dir, tz_str, frequency, users = beiwe_ids)
