import datetime
from airflow import DAG
from airflow.operators import bash_operator

args = {
    'owner' : 'jar_run_one',
    'start_date' : datetime.datetime.now(),
    'provide_context' : True
}
d = datetime.datetime.now()
dag = DAG('jar_run_one' , start_date = d, schedule_interval = '@daily', default_args = args)

t_main = bash_operator.BashOperator(
    task_id = 'running_java_dag' ,
    dag = dag ,
    bash_command = 'javac /opt/airflow/dags/Main.java && java -cp /opt/airflow/dags Main 30000'
)
