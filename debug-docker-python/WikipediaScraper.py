import requests
from bs4 import BeautifulSoup


class WikipediaScraper:
    def get_current_on_this_day_list(self):
        url_to_scrape = 'https://en.wikipedia.org/wiki/Main_Page'
        r = requests.get(url_to_scrape)
        soup = BeautifulSoup(r.text)
        return [li.text for li in soup.select("#mp-otd > ul > li")]


if __name__ == '__main__':
    [print(item) for item in WikipediaScraper().get_current_on_this_day_list()]
