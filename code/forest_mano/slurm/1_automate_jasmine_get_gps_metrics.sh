#!/bin/bash
#
# Usage:
#   1. Make the script executable: chmod +x <NAME_OF_SCRIPT>.sh
#   2. Run it: ./<NAME_OF_SCRIPT>.sh
#
# Description:
#   This script submits SLURM array jobs in consecutive ranges of a specified
#   size. For each range, it calls sbatch with --array, then sleeps for 15
#   minutes before submitting the next batch. It stops once it reaches or
#   exceeds the end index.

###########################
# User-configurable values
###########################

START=13        # First index
END=84         # Last index
BATCH_SIZE=4   # Number of tasks per array batch
SLEEP_TIME=900 # Sleep time in seconds (15 minutes = 900 seconds)

# The SLURM script you want to submit (adjust path as needed)
SLURM_SCRIPT="1_jasmine_get_gps_metrics.sh"

###########################
# Submission logic
###########################

current=$START
while [ $current -le $END ]; do
  # Calculate the end of the current batch
  end_of_batch=$((current + BATCH_SIZE - 1))

  # If the end of this batch goes past END, clamp it to END
  if [ $end_of_batch -gt $END ]; then
    end_of_batch=$END
  fi

  echo "Submitting array job: $current-$end_of_batch"

  # Submit the SLURM job array
  sbatch --array="${current}-${end_of_batch}" "$SLURM_SCRIPT"

  # If we've not reached the final batch, wait before submitting the next one
  if [ $end_of_batch -lt $END ]; then
    echo "Sleeping for $SLEEP_TIME seconds..."
    sleep $SLEEP_TIME
  fi

  # Advance to the next batch
  current=$((end_of_batch + 1))
done

echo "All batches have been submitted."
