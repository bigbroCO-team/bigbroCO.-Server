FROM python:3.12

WORKDIR /app

COPY . .
COPY .env .env

RUN pip install --upgrade pip
RUN pip install -r requirements.txt