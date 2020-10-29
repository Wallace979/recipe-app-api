FROM python:3.8-alpine
LABEL REST Course

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt