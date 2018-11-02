import mysql.connector
import os
import Tweet


class Database:
    def __init__(self):
        database_name = os.getenv("DB_DATABASE", "twitter_persist")
        self.dbconn = mysql.connector.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            user=os.environ["DB_USER"],
            passwd=os.environ["DB_PASS"],
            database=database_name
        )
        self.cursor = self.dbconn.cursor()

    def get_databases(self):
        self.cursor.execute("SHOW DATABASES;")
        return self.cursor

    def get_tables(self):
        self.cursor.execute("SHOW TABLES;")
        return self.cursor

    def create_database(self):
        database_name = os.getenv("DB_DATABASE", "twitter_persist")
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS " + database_name + ";")
        return self.cursor

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tweets (
              id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
              tweet_id BIGINT NOT NULL,
              tweet LONGTEXT NOT NULL,
              created_date DATETIME NOT NULL
            );
            """,
            multi=True
        )
        return self.cursor

    def get_tweets(self):
        self.cursor.execute("SELECT * FROM tweets;")
        return self.cursor

    def insert_tweet(self, tweet: Tweet):
        self.cursor.execute(
            """
            INSERT INTO tweets (tweet_id, tweet)
            VALUES ({0}, "{1}");
            """
            .format(tweet.tweet_id, tweet.tweet)
        )


if __name__ == "__main__":
    db = Database()
    db.create_database()
    db.create_table()
    [print(database) for database in db.get_databases()]
    [print(table) for table in db.get_tables()]
    [print(tweet) for tweet in db.get_tweets()]
