from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'dava',
    'depends_on_past': False,
    'start_date': datetime(2019, 3, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('metalDAG', default_args=default_args, schedule_interval=None)

scrapyMetal = BashOperator(
    task_id='scrapyMetalTask',
    bash_command='/scrapyMetal.sh',
    dag=dag)

