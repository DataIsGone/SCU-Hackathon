#!/usr/bin/env python3

# IndeedScraper.py
# script usage:
# python IndeedScraper.py filename.json "Job Description" "City (optional)" "State (optional)" "zip code (optional)"


import urllib
import requests
import json
from sys import argv


class IndeedScraper:
    _BASE_URL = "https://indreed.herokuapp.com/api/jobs?"

    def __init__(self):
        self._results = []

    @staticmethod
    def _make_url(keywords="", city="", state="", zip_code=""):
        query = urllib.parse.quote(keywords)

        location_unparsed = " ".join([city, state, zip_code])

        location = urllib.parse.quote(location_unparsed)
        url = f"{IndeedScraper._BASE_URL}q={query}&l={location}"
        return url

    def search(self, keywords="", city="", state="", zip_code=""):
        url = IndeedScraper._make_url(keywords, city, state, zip_code)
        response = requests.get(url)
        self._results = response.json()

    def get_results(self):
        return self._results

    def get_result_count(self):
        return len(self._results)

    def save_results_as_json(self, filename):
        with open(filename, 'w') as outfile:
            json.dump(self._results, outfile)


if __name__ == '__main__':
    indeed = IndeedScraper()
    indeed.search(*argv[2:])
    # indeed.save_results_as_json(argv[1])
