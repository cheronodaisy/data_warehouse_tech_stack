from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

# Define your DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 3),
    'email': ['you@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG('Test', default_args=default_args, schedule_interval='@once')

# Define tasks
start_task = DummyOperator(task_id='start_task', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

# Define task sequence
start_task >> end_task
