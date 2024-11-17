from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define the Python function to be run by the PythonOperator
def hello_world():
    print("Hello, World!")

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'simple_hello_world_dag',  # The ID of the DAG
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval='@daily',  # Runs once every day
    start_date=datetime(2024, 11, 11),
    catchup=False,  # Avoid backfilling for missed runs
)

# Define a simple Python task
task_1 = PythonOperator(
    task_id='hello_world_task',  # Task ID
    python_callable=hello_world,  # Python function to execute
    dag=dag,  # Link task to the DAG
)

