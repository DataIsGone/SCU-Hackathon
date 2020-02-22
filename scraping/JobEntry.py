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
        self.title = title
        self.summary = summary
        self.link = link
