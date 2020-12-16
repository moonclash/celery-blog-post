from twitter_service import TwitterService

@app.task(bind=True, name='tweet')
def tweet(self, content):
  twitter_service = TwitterService()
  twitter_service.tweet(content)