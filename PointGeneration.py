# GOOD SHIT


def parse_string(string):
    """ Global function; takes string and parses it into returned list;
        helper function used by modify_score_for_search_term() """
    str_list = []
    i = 0
    word_str = ""
    while i < len(string):
        if not string[i].isspace():
            word_str += string[i]
        else:
            str_list.append(word_str)
            word_str = ""
        i += 1
    return str_list


class PointGeneration:
    """ Scores individual jobs based on specific terms """

    """ Used by base_scoring()
        Lists of terms that determine the base score for each job aggregated;
        job title string is compared to these terms
            * HIGH: base score of 2.5
            * MID: base score of 0
            * LOW: base score of -2.5

        If job title does not have a word that matches any term in these lists,
        it's given a base score of -3 (non-technical job) """

    _BASE_TERMS_LOW = ["support", "technician", "sales"]
    _BASE_TERMS_MID = ["qa", "quality assurance", "analyst", "consultant"]
    _BASE_TERMS_HIGH = ["engineer", "engineering", "developer", "manager"]

    """ Used by apply_modifiers()
        Each key is compared to each word of a job title, and if a term is found,
        the floating point value will be added to the base score """
    _MOD_TERMS = {
        "temp": -1.0,
        "intern": -0.5,
        "junior": 0.5,
        "associate": 0.5,
        "contractor": 0.0,
        "mid-level": 1.0,
        "senior": 1.5,
        "principal": 2.0,
        "director": 2.0
    }

    """ Used by check_for_job_removal()
        Global list that holds all jobs given a base rating """
    _RATED_JOBS = []

    def __init__(self, scraped_list):
        """ Takes list from /scraping/IndeedScraper.py to use in all PointGeneration functions """
        self.job_aggregate_data = scraped_list
        self.total_score = 0

        # Only used by base_scoring(), appended into _RATED_JOBS global list
        # Used to hold job title (key) and base score (value)
        self.job = {}

    def base_scoring(self):
        """ Gives each job a starting score based on job title """
        for job in self.job_aggregate_data:
            for category in job.keys():
                if category == "title":
                    job_title = job.get("title").lower()  # ignoring capitalization
                    if self.check_against_BASE_HIGH(job_title):
                        self.total_score = 2.5
                    elif self.check_against_BASE_LOW(job_title):
                        self.total_score = -2.5
                    elif self.check_against_BASE_MID(job_title):
                        self.total_score = 0
                    else:  # NO RELATED TERMS (IN SCOPE OF PROJECT)
                        self.total_score = -3
                    self.job[job_title] = self.total_score
                    self._RATED_JOBS.append(self.job)

    def check_against_BASE_HIGH(self, job_title):
        """ Used only by base_scoring(); helper function that
            compares each term in _BASE_TERMS_HIGH with each job title """
        for term in self._BASE_TERMS_HIGH:
            if job_title.find(term) != -1:
                return True
        return False

    def check_against_BASE_MID(self, job_title):
        """ Used only by base_scoring(); helper function that
            compares each term in _BASE_TERMS_MID with each job title """
        for term in self._BASE_TERMS_MID:
            if job_title.find(term) != -1:
                return True
        return False

    def check_against_BASE_LOW(self, job_title):
        """ Used only by base_scoring(); helper function that
            compares each term in _BASE_TERMS_LOW with each job title """
        for term in self._BASE_TERMS_LOW:
            if job_title.find(term) != -1:
                return True
        return False

    def apply_modifiers(self):
        """ Applies modifier floats from _MOD_TERMS """
        for job in self.job_aggregate_data:
            for category in job.keys():
                if category == "title":
                    job_title = job.get("title").lower()
                    for term in self._MOD_TERMS:
                        if (job_title.find(term) != -1) and (not self.check_for_removal(job_title)):
                            self.total_score += self._MOD_TERMS[term]

    def check_for_removal(self, job_title):
        """ Helper function used by only apply_modifiers();
            checks to see if a job has a base score of -3 or lower
            and ignores applying modifiers if so """
        for jobs in self._RATED_JOBS:  # job is a dict
            for title in jobs.keys():
                if title == job_title:
                    if jobs[title] <= -3:
                        return True  # should be removed
                    return False  # should not be removed

    def modify_score_for_search_term(self, search_term):
        """ Checks the job summary to see if any words match the provided search term """
        count = 0
        for job in self.job_aggregate_data:
            for category in job.keys():
                if category == "summary":
                    summary = parse_string(job.get("summary").lower())  # ignore capitalization
                    for word in summary:
                        if word == search_term.lower():
                            count += 1
                            print("count: " + str(count))
        search_term_modifier = 0.25 * count
        self.total_score += search_term_modifier


def main():
    pass
    # test_point_gen = PointGeneration('jsonTest_techFocus')
    # test_point_gen.base_scoring()
    # test_point_gen.apply_modifiers()
    # test_point_gen.modify_score_for_search_term("support")


if __name__ == "__main__":
    main()
