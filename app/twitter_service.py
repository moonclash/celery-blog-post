import os
import tweepy
from random import randrange

class TwitterService(object):

  RANDOM_STATUSES = [
    'This is a random tweet',
    'I genuinely do not know why twitter is such hype',
    'Potato pancakes are great',
    'Blueberries',
    'Strawberries',
    'Digital rubber ducking is really cool!'
  ]
  
  def __init__(self):
    auth = tweepy.OAuthHandler(os.environ.get('TWITTER_CONSUMER_API'), os.environ.get('TWITTER_CONSUMER_SECRET'))
    auth.set_access_token(os.environ.get('TWITTER_API_KEY'), os.environ.get('TWITTER_API_SECRET'))
    self.api = tweepy.API(auth)
  
  def tweet(self, text):
    self.api.update_status(status=text)
    return
  
  def random_tweet(self, time):
    statuses = self.RANDOM_STATUSES
    try:
      self.tweet(text=f'{statuses[randrange(0, len(statuses))]} , automated by celery, posted @ {time}')
    except tweepy.error.TweepError:
      self.tweet('ooops')


