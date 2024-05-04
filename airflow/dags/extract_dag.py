from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime
from extract import Extract
from dotenv import load_dotenv
import os

load_dotenv()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 4),
    'retries': 1
}

def extract_and_load_to_db():
    extractor = Extract("../data/20181024_d1_0830_0900.csv")
    df_track, df_trajectory = extractor.extract_data()
    extractor.save_to_postgres(df_track, df_trajectory, host='localhost', database='traffic', user='daisy', password=os.getenv('PG_PASSWORD'))

dag = DAG(
    'traffic_data_pipeline',
    default_args=default_args,
    description='A DAG to process traffic data',
    schedule_interval=None,
)

extract_and_load_task = PythonOperator(
    task_id='extract_and_load_to_db',
    python_callable=extract_and_load_to_db,
    dag=dag,
)

extract_and_load_task
