from Database import Database
from TwitterHandler import TwitterHandler
from Tweet import Tweet


class App():
    def __init__(self):
        self.db = Database()
        self.th = TwitterHandler()

    def main(self):
        tweets = self.th.home()
        [self.persist_tweet(tweet) for tweet in tweets]
        [print(tweet) for tweet in self.db.get_tweets()]

    def persist_tweet(self, tweet):
        self.db.insert_tweet(Tweet(tweet['id'], tweet['text']))


if __name__ == '__main__':
    App().main()
