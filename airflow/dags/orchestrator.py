from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append('/opt/airflow/api-request')

def safe_main_callable():
    from insert_records import main
    return main()

default_args = {
    'start_date':datetime(2025,9,24),
    'retries':1,
    'retry_delay':timedelta(minutes=5)
    }

dag = DAG(
    dag_id = 'weather-api-orchestrator',
    default_args=default_args,
    description = 'A DAG to orchestrate data',
    schedule_interval=timedelta(minutes=10),
    catchup=False
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )