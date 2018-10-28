import unittest
from app import App
from WikipediaScraper import WikipediaScraper
from io import StringIO


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.app = App()
        self.ws = WikipediaScraper()

    def testWikipediaScraper(self):
        otd_items = WikipediaScraper().get_current_on_this_day_list()
        self.assertGreater(len(otd_items), 0)

    def testApp(self):
        otd_items = WikipediaScraper().get_current_on_this_day_list()
        out = StringIO()
        self.app.run(out)
        self.assertEqual(out.getvalue().strip(), "".join(otd_items))


if __name__ == '__main__':
    unittest.main()
