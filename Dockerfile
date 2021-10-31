FROM ubuntu:focal

RUN apt update
RUN apt -y install python3 pip mysql-client

RUN mkdir /www
RUN mkdir /www/app

COPY requirements.txt /www/app/

RUN pip install -r /www/app/requirements.txt

COPY . /www/app/

RUN ls /www/app/frontend/taskmanager

ENTRYPOINT sh /www/app/docker-entrypoint.sh
