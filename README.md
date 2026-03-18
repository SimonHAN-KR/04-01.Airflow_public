# 04.Airflow

[GitHub - apache/airflow: Apache Airflow - A platform to programmatically author, schedule, and monitor workflows](https://github.com/apache/airflow)

[apache/airflow - Docker Image](https://hub.docker.com/r/apache/airflow)

- docker 불러오기
  docker pull apache/airflow:3.1.5-python3.13
  docker pull apache/airflow:slim-3.1.5-python3.13
- docker-composer 불러오기


## docker-compose.yaml 불러오기
#- 리눅스
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.1.5/docker-compose.yaml'

#- 윈도우 powershell
Invoke-WebRequest -Uri https://airflow.apache.org/docs/apache-airflow/3.1.5/docker-compose.yaml -Outfile D:\OneDrive_VIBEON\91.Programs\04.Airflow\docker-compose.yaml


## docker-compose.yaml 변경
# airflow 슬림 버전
image: ${AIRFLOW_IMAGE_NAME:-airflow:slim-3.1.5-python3.13}
# 예제 DAG LOAD 안 불러오기
AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
# DB연결
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://postgres:postgre0213@192.168.0.99:5432/airflow262

## .env 파일 생성
# 내용
AIRFLOW_UID=50000
_AIRFLOW_WWW_USER_USERNAME=simon
_AIRFLOW_WWW_USER_PASSWORD=simon


## .yaml 파일 기반 docker 설치
sudo docker compose up

## docker file 적용하고 실행
sudo docker compose build
sudo docker compose up -d

## docker 컨테이너 및 이미지 삭제
sudo docker compose down --volumes --rmi all


## 예제파일 안불러오기
# airflow.cfg
load_examples = False
