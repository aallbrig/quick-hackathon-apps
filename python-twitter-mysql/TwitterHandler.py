from twitter import *
import os


class TwitterHandler:
    def __init__(self):
        self.t = Twitter(
            auth=OAuth(
                os.environ['TWITTER_TOKEN'],
                os.environ['TWITTER_TOKEN_SECRET'],
                os.environ['TWITTER_CONSUMER_KEY'],
                os.environ['TWITTER_CONSUMER_SECRET']
            )
        )

    def home(self):
        return self.t.statuses.home_timeline()


if __name__ == '__main__':
    th = TwitterHandler()
    [print(tweet) for tweet in th.home()]
