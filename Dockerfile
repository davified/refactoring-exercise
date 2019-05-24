FROM python:3.6-slim

RUN apt-get update \
  && apt-get install -y curl git

WORKDIR /home/clean-code-data-science

COPY . /home/clean-code-data-science
RUN pip install -U pip && pip install -r requirements.txt
