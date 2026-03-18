from airflow import DAG
# from airflow.providers.postgres.operators.postgres import PostgresOperator
# from airflow.sensors.sql import SqlSensor
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.common.sql.sensors.sql import SqlSensor
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 7, 1)
}

# Define the DAG
with DAG(
    dag_id="postgres_loader",
    description="PostgreSQL Loader Example",
    default_args=default_args,
    schedule="0 0 * * *",
    catchup=False,
) as dag:
    # Task: Execute a SQL query using PostgresOperator
    sql_query = """
        INSERT INTO sample_table (key, value)
        VALUES ('hello', 'world')
    """

    # postgres_task = PostgresOperator(
    postgres_task = SQLExecuteQueryOperator(
        task_id='execute_sql_query',
        conn_id='my_postgres_connection',
        sql=sql_query,
        dag=dag
    )

    sql_sensor = SqlSensor(
        task_id='wait_for_condition',
        conn_id='my_postgres_connection',
        sql="SELECT COUNT(*) FROM sample_table WHERE key='hello'",
        mode='poke',
        poke_interval=30,
        dag=dag
    )
    
    sql_query_confirm = """
        INSERT INTO sample_table (key, value)
        VALUES ('sensor', 'confirmed')
    """

    # postgres_confirm_task = PostgresOperator(
    postgres_confirm_task = SQLExecuteQueryOperator(
        task_id='execute_sql_confirm_query',
        conn_id='my_postgres_connection',
        sql=sql_query_confirm,
        dag=dag
    )
    
postgres_task >> sql_sensor >> postgres_confirm_task
