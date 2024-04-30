"""
Script to extract data from a csv file with unequal columns.
It extracts the data into two dataframes suitable for a relational database.

Author: Daisy Cherono
Date: 4/30/2024

Dependencies:
    - pandas
Usage:
    Ensure that all dependencies are installed:
        conda install pandas
    Run the script:
        python extract.py
"""

import pandas as pd

with open("../data/20181024_d1_0830_0900.csv", 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(f"The number of rows/lines is {len(lines)}")

lines_as_lists = [
    line.strip('\n').strip().strip(';').split(';') for line in lines
    ]
len(lines_as_lists)

NO_FIELD_MAX = 0

for row in lines_as_lists:
    if len(row) > NO_FIELD_MAX:
        no_field_max = len(row)

print(f"the maximum number of fields is {NO_FIELD_MAX}")
LARGEST_N = int((NO_FIELD_MAX-4)/6)
print(f"the largest n = {LARGEST_N}")

cols = lines_as_lists.pop(0)

track_cols = cols[:4]
trajectory_cols = ['track_id'] + cols[4:]

print(track_cols)
print(trajectory_cols)

track_info = []
trajectory_info = []

for row in lines_as_lists:
    track_id = row[0]

    # add the first 4 values to track_info
    track_info.append(row[:4])

    remaining_values = row[4:]
    # reshape the list into a matrix and add track_id
    trajectory_matrix = [[track_id] + remaining_values[i:i+6]
                         for i in range(0, len(remaining_values), 6)]
    # add the matrix rows to trajectory_info
    trajectory_info = trajectory_info + trajectory_matrix

df_track = pd.DataFrame(data=track_info, columns=track_cols)

print(df_track.head())

df_trajectory = pd.DataFrame(data=trajectory_info, columns=trajectory_cols)

print(df_trajectory.head())
