from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email_on_failure': True,
    'email_on_retry': True,
    'email': ['malkiacoder@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dbt_dag',
    default_args=default_args,
    description='A DAG to run dbt commands',
    schedule=timedelta(days=1),
)

def run_dbt_command(dbt_command):
    try:
        subprocess.run(dbt_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing dbt command: {e}")

run_dbt_fast_vehicles = PythonOperator(
    task_id='run_dbt_fast_vehicles',
    python_callable=run_dbt_command,
    op_kwargs={'dbt_command': 'dbt run --models fast_vehicles'},
    dag=dag,
)

run_dbt_traffic_details = PythonOperator(
    task_id='run_dbt_traffic_details',
    python_callable=run_dbt_command,
    op_kwargs={'dbt_command': 'dbt run --models traffic_details'},
    dag=dag,
)

run_dbt_vehicle_details = PythonOperator(
    task_id='run_dbt_vehicle_details',
    python_callable=run_dbt_command,
    op_kwargs={'dbt_command': 'dbt run --models vehicle_details'},
    dag=dag,
)

run_dbt_fast_vehicles >> run_dbt_traffic_details
run_dbt_fast_vehicles >> run_dbt_vehicle_details
