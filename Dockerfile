FROM python:3.8

WORKDIR /celery-app/celery-tut

COPY . .

RUN pip3 install -r requirements.txt
