FROM node:lts-stretch

RUN apt update

RUN mkdir /www
RUN mkdir /www/app

COPY ./package.json /www/app/package.json

WORKDIR /www/app

RUN yarn install --production=false

COPY ./ /www/app/

RUN rm yarn.lock

ENTRYPOINT sh docker-entrypoint.sh
