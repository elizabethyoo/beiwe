#!/bin/bash

# submit series of job arrays from index 0 to 84 in increments of 3, with 30min breaks bw each submission
for (( start=0; start<=84; start+=3 ))
do
  end=$(( start + 3 ))
  if [ "$end" -gt 84 ]; then
    end=84
  fi
  echo "Submitting job array $start-$end"
  sbatch --array=${start}-${end} manual_download.sh
  sleep 30m
done