from celery import Celery
from .twitter_service import TwitterService

app = Celery(
  broker='amqp://guest:guest@rabbit_mq:5672/%2F'
)

@app.task(bind=True, name='tweet')
def tweet(self, time):
  twitter_service = TwitterService()
  twitter_service.random_tweet(time)
