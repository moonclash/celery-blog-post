from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@rabbit_mq:5672/%2F')

@app.task
def add(x, y):
  return x + y