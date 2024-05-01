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
import psycopg2
from sqlalchemy import create_engine

class Extract:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def extract_data(self):
        with open(self.csv_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lines_as_lists = [
            line.strip('\n').strip().strip(';').split(';') for line in lines
        ]

        track_cols = lines_as_lists[0][:4]
        trajectory_cols = ['track_id'] + lines_as_lists[0][4:]

        track_info = []
        trajectory_info = []

        for row in lines_as_lists[1:]:
            track_id = row[0]
            track_info.append(row[:4])

            remaining_values = row[4:]
            trajectory_matrix = [[track_id] + remaining_values[i:i+6]
                                 for i in range(0, len(remaining_values), 6)]
            trajectory_info.extend(trajectory_matrix)

        df_track = pd.DataFrame(data=track_info, columns=track_cols)
        df_trajectory = pd.DataFrame(data=trajectory_info, columns=trajectory_cols)

        return df_track, df_trajectory

    # def save_to_postgres(self, df_track, df_trajectory, host, database, user, password):
    #     try:
    #         conn = psycopg2.connect(
    #             host=host,
    #             database=database,
    #             user=user,
    #             password=password
    #         )
    #         cursor = conn.cursor()

    #         # Create tables
    #         cursor.execute('''
    #             CREATE TABLE IF NOT EXISTS track (
    #                 track_id INTEGER PRIMARY KEY,
    #                 type VARCHAR(255),
    #                 traveled_d FLOAT,
    #                 avg_speed FLOAT
    #             )
    #         ''')

    #         cursor.execute('''
    #             CREATE TABLE IF NOT EXISTS trajectory (
    #                 track_id INTEGER,
    #                 lat FLOAT,
    #                 lon FLOAT,
    #                 speed FLOAT,
    #                 lon_acc FLOAT,
    #                 lat_acc FLOAT,
    #                 time FLOAT
    #             )
    #         ''')

    #         # Insert data
    #         df_track.to_sql('track', conn, if_exists='append', index=False)
    #         df_trajectory.to_sql('trajectory', conn, if_exists='append', index=False)

    #         conn.commit()
    #         print("Data inserted successfully into PostgreSQL")

    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print("Error while working with PostgreSQL", error)
    #     finally:
    #         if conn is not None:
    #             conn.close()


   # Other methods remain the same...

    def save_to_postgres(self, df_track, df_trajectory, host, database, user, password):
        try:
            # Create SQLAlchemy engine
            engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')

            # Create tables
            df_track.to_sql('track', engine, if_exists='append', index=False)
            df_trajectory.to_sql('trajectory', engine, if_exists='append', index=False)

            print("Data inserted successfully into PostgreSQL")

        except Exception as e:
            print("Error while working with PostgreSQL:", e)

from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv('PG_PASSWORD')

# Usage example
if __name__ == "__main__":
    extractor = Extract("../data/20181024_d1_0830_0900.csv")
    df_track, df_trajectory = extractor.extract_data()
    extractor.save_to_postgres(df_track, df_trajectory, host='localhost', database='traffic', user='daisy', password=password)
