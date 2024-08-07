FROM python:3.12

WORKDIR /app

COPY . .

RUN apt install mysqlclient
RUN apt install libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt