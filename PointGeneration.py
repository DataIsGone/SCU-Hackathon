import json


def get_json(file):
    try:
        with open(file, 'r') as infile:
            job_list = json.load(infile)
            return job_list
    except FileNotFoundError:
        print("File not found")


def parse_string(string):
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
    _BASE_TERMS_LOW = ["support", "technician", "sales"]
    _BASE_TERMS_MID = ["qa", "quality assurance", "analyst", "consultant"]
    _BASE_TERMS_HIGH = ["engineer", "engineering", "developer", "manager"]

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

    _RATED_JOBS = []

    def __init__(self, file):
        self.json_file = get_json(file)
        self.total_score = 0
        self.job = {}

    def base_scoring(self):
        for job in self.json_file:
            for category in job.keys():
                if category == "title":
                    job_title = job.get("title").lower()
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
        for term in self._BASE_TERMS_HIGH:
            if job_title.find(term) != -1:
                return True
        return False

    def check_against_BASE_MID(self, job_title):
        for term in self._BASE_TERMS_MID:
            if job_title.find(term) != -1:
                return True
        return False

    def check_against_BASE_LOW(self, job_title):
        for term in self._BASE_TERMS_LOW:
            if job_title.find(term) != -1:
                return True
        return False

    def apply_modifiers(self):
        for job in self.json_file:
            for category in job.keys():
                if category == "title":
                    job_title = job.get("title").lower()
                    for term in self._MOD_TERMS:
                        if (job_title.find(term) != -1) and (not self.check_for_removal(job_title)):
                            self.total_score += self._MOD_TERMS[term]

    def check_for_removal(self, job_title):
        for jobs in self._RATED_JOBS:  # job is a dict
            for title in jobs.keys():
                if title == job_title:
                    if jobs[title] <= -3:
                        return True  # should be removed
                    return False  # should not be removed

    def modify_score_for_search_term(self, search_term):
        count = 0
        for job in self.json_file:
            for category in job.keys():
                if category == "summary":
                    summary = parse_string(job.get("summary").lower())
                    for word in summary:
                        if word == search_term.lower():
                            count += 1
                            print("count: " + str(count))
        search_term_modifier = 0.25 * count
        self.total_score += search_term_modifier
        print(summary)
        print(": " + str(self.total_score))


def main():
    test_point_gen = PointGeneration('jsonTest_techFocus')
    test_point_gen.base_scoring()
    test_point_gen.apply_modifiers()
    test_point_gen.modify_score_for_search_term("support")

if __name__ == "__main__":
    main()
