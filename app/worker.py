from celery import Celery
app = Celery(
  broker='amqp://guest:guest@rabbit_mq:5672/%2F',
  include=['tasks']
)

app.conf.beat_schedule = {
  'tweet': {
    'task': 'tweet',
    'schedule': '300.0',
    'args': ([
      'Hey, i automated my twitter with celery!'
    ]),
  },
}
