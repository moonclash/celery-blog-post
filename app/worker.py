from celery import Celery
from datetime import datetime

app = Celery(
  broker='amqp://guest:guest@rabbit_mq:5672/%2F',
)

app.conf.beat_schedule = {
  'tweet': {
    'task': 'tweet',
    'schedule': 30.0,
    'args': ([
      datetime.now(),
    ]),
  },
}
