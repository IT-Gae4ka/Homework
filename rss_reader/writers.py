from .rss_item import RssItem
from .utils import Console, date_to_str, NewsEncoder, open_cache_file_for_write
from abc import ABCMeta, abstractmethod
import csv
import logging


class Writer(metaclass=ABCMeta):
    """Abstract class with write method. Takes news."""
    @abstractmethod
    def write(self, news):
        """Abstract method for writing."""
        pass


class CacheWriter(Writer):
    """Writes cache from RssStorage object."""
    def write(self, news):
        logging.info('Running write() function. Class CacheWriter(Writer).')
        with open_cache_file_for_write() as f:
            csv_writer = csv.writer(f, delimiter=',')

            for item in news:
                csv_writer.writerow([item.title, date_to_str(item.date),
                                    item.link])


class JsonWriter(Writer):
    """Writes news into console in json format"""
    def write(self, news):
        logging.info('Running write() function. Class JsonWriter(Writer).')
        encoder = NewsEncoder(indent=2, ensure_ascii=False)
        with Console() as console:
            console.write(encoder.encode(list(news)))


class ConsoleWriter(Writer):
    """Writes news into console."""
    def write(self, news):
        logging.info('Running write() function. Class ConsoleWriter(Writer).')
        with Console() as console:
            for item in news:
                title = item.title
                date = date_to_str(item.date)
                link = item.link
                console.write(f"Title: {title}\n\nDate: {date}\n\nLink: {link}\n\n\
                --------------\n\n")
