FROM ubuntu:latest

RUN apt update && apt install python3 -y

RUN pip install -r requirements.txt

CMD ["python3", "./manage.py", "runserver"]