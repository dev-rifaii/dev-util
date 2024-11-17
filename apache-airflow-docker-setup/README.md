# Apache Airflow Docker setup

A docker compose file that will start an airflow webserver, airflow scheduler and a postgres database.

The official apache airflow image does not come with JRE or JDK included thus the image used for webserver and scheduler is altered in the Dockerfile to include JDK 17 in order to run Java DAGs and neovim for easier file editing during testing.

```
docker compose -f airflow.yaml up
```
