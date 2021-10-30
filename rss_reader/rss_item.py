from datetime import datetime


class RssItem:
    """Class for temprary storage of title, date and link."""
    def __init__(self, title, date, link):
        assert(isinstance(title, str))
        self.title = title
        assert(isinstance(date, datetime))
        self.date = date
        assert(isinstance(link, str))
        self.link = link
