from airflow import DAG
from airflow.operators.dummy import DummyOperator

from datetime import datetime

user = "2rp-muriloa" 

default_args = {
    "owner": user,
    "start_date": datetime(2023,1,24),
}

with DAG(dag_id='de_murilo_andrade_dev', default_args=default_args, catchup=False) as dag:

    testDummyOperator = DummyOperator(
        task_id='testDummyOperator'
    )
