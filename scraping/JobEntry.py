class JobEntry:
    """Defines standard class job entry (site agnostic)."""

    def __init__(self, title, summary, link):
        """Create object of type JobEntry.

        Parameters
        ----------
        title: str
            Title of job from website.
        summary: str
            Short description of job.
        link: str
            URL for job listing.
        """
        self._title = title
        self._summary = summary
        self._link = link

    def get_title(self):
        return self._title

    def get_summary(self):
        return self._summary

    def get_link(self):
        return self._link
