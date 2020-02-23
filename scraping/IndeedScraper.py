import urllib
import requests


class IndeedScraper:
    _BASE_URL = "https://indreed.herokuapp.com/api/jobs?"

    def __init__(self):
        self.results = []  # List of found Job entries

    @staticmethod
    def _make_url(keywords="", city="", state="", zip_code=""):
        query = urllib.parse.quote(keywords)

        location_unparsed = " ".join([city, state, zip_code])

        location = urllib.parse.quote(location_unparsed)

        url = f"{IndeedScraper._BASE_URL}q={query}&l={location}"
        return url

    def search(self, keywords="", city="", state="", zip_code=""):
        response = requests.get(self._make_url(keywords, city,
                                               state, zip_code))
        return response.json()


if __name__ == '__main__':
    indeed = IndeedScraper()
    results = indeed.search("chemistry", "Oakland", "CA")
