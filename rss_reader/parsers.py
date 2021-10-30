from .utils import date_from_str, get_url_contents, open_cache_file_for_read
from .rss_item import RssItem
from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod
import csv
import logging


class RssParser(metaclass=ABCMeta):
    """Abstract class.
    Has abstract method read news."""
    @abstractmethod
    def read_news(self):
        """Abstract method for reading news"""
        pass


class WebRssParser(RssParser):
    """Takes url as an argument.
    Creates b4s object in xml."""
    def __init__(self, url):
        contents = get_url_contents(url)
        self._soup = BeautifulSoup(contents, 'xml')

    def read_news(self):
        """Reads news from b4s object."""
        logging.info('Running read_news() function.\
                     Class WebRssParser(RssParser).')
        items = self._soup.find_all('item')

        for item in items:
            title = item.title.text
            date = date_from_str(item.pubDate.text)
            link = item.link.text
            yield RssItem(title, date, link)


class CacheRssParser(RssParser):
    """Takes news from csv file."""
    def read_news(self):
        """Reads news from csv file."""
        logging.info('Running read_news() function.\
                     Class CacheRssParser(RssParser).')
        with open_cache_file_for_read() as f:
            csv_reader = csv.reader(f, delimiter=',')

            for row in csv_reader:
                if row:
                    yield RssItem(row[0], date_from_str(row[1]), row[2])
