import os
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'dava',
    'depends_on_past': False,
    'start_date': datetime(2019, 3, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('metalDAG', default_args=default_args, schedule_interval=None)

def metalPath():
    for root, dirs, files in os.walk("/Users/dava/Documentos/Python/ScrapyMetal"):
        for file in files:
            if file.endswith(".csv"):
                path = os.path.join(root, file)
    return path

scrapyMetal = BashOperator(
    task_id='scrapyMetalTask',
    bash_command='/scrapyMetal.sh',
    dag=dag)

metalPath = PythonOperator(
    task_id='metalPathTask',
    python_callable=metalPath,
    dag=dag
)

scrapyMetal>>metalPath