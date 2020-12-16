from celery import Celery
from datetime import datetime

app = Celery(
  broker='amqp://guest:guest@rabbit_mq:5672/%2F',
  include=['tasks']
)

app.conf.beat_schedule = {
  'tweet': {
    'task': 'tweet',
    'schedule': '300.0',
    'args': ([
      f'Hello! This is an automated tweet with celery posted at {datetime.now()}'
    ]),
  },
}
