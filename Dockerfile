FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install mysqlclient
RUN apt install default-libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt