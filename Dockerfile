FROM ubuntu:focal

RUN apt update
RUN apt -y install python3 pip mysql-client

RUN mkdir /www
RUN mkdir /www/app

COPY ./ /www/app/

RUN pip install -r /www/app/requirements.txt

RUN ls /www/app

ENTRYPOINT sh /www/app/docker-entrypoint.sh
