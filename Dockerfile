FROM python:3.6-slim

RUN apt-get update \
  && apt-get install -y curl git

RUN git config --global user.email "your@email.com"
RUN git config --global user.name "your-github-username"

xx
# update the lines above with your git username and email before running `docker build`

WORKDIR /home/clean-code-ml

COPY . /home/clean-code-ml
RUN pip install -U pip && pip install -r requirements.txt
