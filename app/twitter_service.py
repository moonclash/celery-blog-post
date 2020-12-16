import os
import tweepy

class TwitterService(object):
  
  def __init__(self):
    auth = tweepy.OAuthHandler(os.environ.get('TWITTER_CONSUMER_API'), os.environ.get('TWITTER_CONSUMER_SECRET'))
    auth.set_access_token(os.environ.get('TWITTER_API_KEY'), os.environ.get('TWITTER_API_SECRET'))
    self.api = tweepy.API(auth)
  
  def tweet(self, text):
    self.api.update_status(status=text)
    return

