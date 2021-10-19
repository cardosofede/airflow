from airflow import DAG
from airflow.operators.python import task
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.example import example_function



default_args = {
    'email': ['federico.cardoso.e@gmail.com'],
    'email_on_failure': True,
    'retries': 2,
    'retry_delay':timedelta(minutes=5)
}
with DAG(
    'example_dag',
    start_date=datetime(2021, 8, 12),
    schedule_interval='0 0 * * *',
    default_args=default_args,
    catchup=False) as dag:

    etl_hummingbot = PythonOperator(
        task_id='example_task',
        python_callable=example_function,
        op_kwargs={'args': 'test'}
    )


    etl_hummingbot

