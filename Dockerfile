FROM python:3.6-slim

RUN apt-get update

WORKDIR /code
COPY . /code

RUN pip install -U pip && pip install -r requirements.txt
