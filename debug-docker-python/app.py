import sys
from WikipediaScraper import WikipediaScraper


class App:
    def __init__(self):
        self.ws = WikipediaScraper()

    def run(self, out=sys.stdout):
        [out.write(item) for item in self.ws.get_current_on_this_day_list()]


if __name__ == '__main__':
    App().run()
