from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta
from extract import Extract
from dotenv import load_dotenv
import os

load_dotenv()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 4),
    'email_on_failure': True,
    'email_on_retry': True,
    'email': ['malkiacoder@gmail.com'],
    'catchup': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_and_load_to_db():
    extractor = Extract("/home/daisy/Desktop/tenx/data_warehouse_tech_stack/data/20181024_d1_0830_0900.csv")
    df_track, df_trajectory = extractor.extract_data()
    extractor.save_to_postgres(df_track, df_trajectory, host='localhost', database='traffic', user='daisy', password=os.getenv('PG_PASSWORD'))

dag = DAG(
    'traffic_data_pipeline',
    default_args=default_args,
    description='A DAG to process traffic data',
    schedule=timedelta(days=1),
)

extract_and_load_task = PythonOperator(
    task_id='extract_and_load_to_db',
    python_callable=extract_and_load_to_db,
    dag=dag,
)

extract_and_load_task
