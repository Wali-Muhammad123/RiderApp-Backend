FROM postgres:14

COPY ./scripts/setup.sh  /docker-entrypoint-initdb.d/1.sh
RUN apt-get update && apt-get install -y postgis
RUN chmod +x /docker-entrypoint-initdb.d/1.sh