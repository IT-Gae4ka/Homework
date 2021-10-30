from .rss_item import RssItem
from datetime import datetime
from urllib.parse import urlparse
from abc import ABCMeta, abstractmethod
import logging


class NewsFilter(metaclass=ABCMeta):
    """Abstract class with abstract method check_news"""
    @abstractmethod
    def check_news(self, news):
        """Abstract method for checking news."""
        pass


class DateFilter(NewsFilter):
    """Takes date as an argument.
    Has method check_news."""
    def __init__(self, date):
        assert(isinstance(date, datetime))
        self._date = date

    def check_news(self, news):
        """Checks wheather the news has the requested date"""
        logging.info('Running check_news() function.\
                     Class DateFilter(NewsFilter).')
        assert(isinstance(news, RssItem))
        return news.date.date() == self._date.date()


class SourceFilter(NewsFilter):
    """Takes source as an argument.
    Has method check_news."""
    def __init__(self, source):
        assert(isinstance(source, str))
        self._netloc = urlparse(source).netloc

    def check_news(self, news):
        """Checks wheather the news has the requested source."""
        logging.info('Running check_news() function.\
                    Class SourceFilter(NewsFilter).')
        assert(isinstance(news, RssItem))
        return urlparse(news.link).netloc == self._netloc
