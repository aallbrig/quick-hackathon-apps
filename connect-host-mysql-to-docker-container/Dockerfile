FROM ubuntu:latest

ENV DB_HOSTNAME="host.docker.internal"
ENV DB_USERNAME="root"
ENV DB_PASSWORD=""

RUN apt-get update -yqq \
    && apt-get install mysql-server -yqq

CMD mysql -h$DB_HOSTNAME -u$DB_USERNAME -e "SHOW DATABASES;"
