FROM ubuntu:latest

RUN apt update && apt install -y python3

RUN pip install -r requirements.txt

CMD ["python3", "./manage.py", "runserver"]