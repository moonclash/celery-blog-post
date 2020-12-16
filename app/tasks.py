from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', backend='rpc://', broker='amqp://guest:guest@rabbit_mq:5672/%2F')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
  sender.add_periodic_task(
    crontab(minute=1),
    add.s(5, 5)
  )


@app.task
def add(x, y):
  print(x, y)
  return x + y