import urllib


class IndeedScraper:
    _BASE_URL = 'https://www.indeed.com/jobs?'

    def __init__(self):
        self.results = []  # List of found Job entries

    @staticmethod
    def _make_url(keywords="", city="", state="", zip_code=""):
        base_url = 'https://www.indeed.com/jobs?'
        query = urllib.parse.quote(keywords)

        location_unparsed = " ".join([city, state, zip_code])

        location = urllib.parse.quote(location_unparsed)

        url = f"{base_url}q={query}&l={location}"  # &radius={radius}"
        return url
