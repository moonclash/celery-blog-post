FROM python:3.8

WORKDIR /app/celery-tut

COPY . .

RUN pip3 install -r requirements.txt
