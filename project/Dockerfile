FROM python:3.8-alpine

WORKDIR /project

COPY requirements.txt /project
RUN pip install -r requirements.txt

COPY . /project

ENV PYTHONUNBUFFERED 1



