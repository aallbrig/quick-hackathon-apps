from Database import Database
from TwitterHandler import TwitterHandler


class App():
    def __init__(self):
        self.db = Database()
        self.th = TwitterHandler()
        self.greeting = 'App!'

    def main(self):
        print(self.greeting)


if __name__ == '__main__':
    App().main()
