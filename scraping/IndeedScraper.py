import urllib


class IndeedScraper:
    _BASE_URL = 'https://www.indeed.com/jobs?'

    def __init__(self):
        self.results = []  # List of found Job entries

    def _make_url(keywords="", city="", state="", zip_code=""):
        base_url = 'https://www.indeed.com/jobs?'
        query = urllib.parse.quote(keywords)

        location_unparsed = city  # assume user will always enter a i

        if state != "":
            location_unparsed += f", {state}"
        if zip_code != "":
            location_unparsed += f" {zip_code}"

            location = urllib.parse.quote(location_unparsed)

        location = urllib.parse.quote(city)
        url = f"{base_url}q={query}&l={location}"  # &radius={radius}"
        return url
