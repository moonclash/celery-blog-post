from twitter_service import TwitterService
from datetime import datetime

@app.task(bind=True, name='tweet')
def tweet(self, content):
  twitter_service = TwitterService()
  twitter_service.tweet(f'Hello! This is an automated tweet with celery posted at {datetime.now()}')