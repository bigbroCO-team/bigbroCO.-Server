FROM python:3.12

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install poetry

RUN poetry install --no-root

ARG DJANGO_SETTINGS_MODULE
