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
        """Make a valid Indreed URL for job searches.

        Parameters
        ----------
        keywords: str
            String (len <= 50) that describes the job to search for.
        city: str
            String (len <= 50) for the city to search near.
        state: str
            String (len <= 2) for US State abbreviation.
        zip_code: str
            Zip code to search nearby.

        Returns
        -------
        Str
            Valid search string for indreed.com.
        """
        query = urllib.parse.quote(keywords)

        location_unparsed = " ".join([city, state, zip_code])

        location = urllib.parse.quote(location_unparsed)
        url = f"{IndeedScraper._BASE_URL}q={query}&l={location}"
        return url

    def search(self, keywords="", city="", state="", zip_code=""):
        """Performs a search of Indeed.com using Indreed REST-API.

        Searches for a maximum of 20 job search results.

        Updates self._results as list of dct.

        Parameters
        ----------
        keywords: str
            String (len <= 50) that describes the job to search for.
        city: str
            String (len <= 50) for the city to search near.
        state: str
            String (len <= 2) for US State abbreviation.
        zip_code: str
            Zip code to search nearby.

        Returns
        -------
        None
        """
        url = IndeedScraper._make_url(keywords, city, state, zip_code)
        response = requests.get(url)
        self._results = response.json()

    def get_results(self):
        """Getter

        Returns
        -------
        List of dict
            List of dictionaries of top at most 20 job search reuslts.
        """
        return self._results

    def get_result_count(self):
        """Counts number of results in most recent job search.

        Returns
        -------
         int
            Number of results from most recent search.
        """
        return len(self._results)

    def save_results_as_json(self, filename):
        """Saves most recent results as a JSON file.



        Parameters
        ----------
        filename: str
            Name of file to write the data to.

        Returns
        -------
        None
        """
        with open(filename, 'w') as outfile:
            json.dump(self._results, outfile)


if __name__ == '__main__':
    indeed = IndeedScraper()
    indeed.search(*argv[2:])
    indeed.save_results_as_json(argv[1])
