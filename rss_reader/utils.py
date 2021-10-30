import requests
import sys
import json
from rss_item import RssItem
from datetime import datetime
import logging


def get_url_contents(url):
    """Gets news feed"""
    logging.info('Running get_url_contents() function from utils.py.')
    res = requests.get(url)
    if not res.ok:
        raise Exception('GET error in {}', url)
    return res.content


def open_cache_file_for_read():
    """Opens csv file for reading news from cache."""
    logging.info('Running open_cache_file_for_read() function from utils.py.')
    return open('articles.csv', 'r', newline='', encoding='utf-8')


def open_cache_file_for_write():
    """Opens csv file for writhing cache."""
    logging.info('Running open_cache_file_for_write() function from utils.py.')
    return open('articles.csv', 'a', newline='', encoding='utf-8')


def date_from_str(s):
    """Changes format of date from string to %Y%m%d"""
    logging.info('Running date_from_str() function from utils.py.')

    assert(isinstance(s, str))

    s = s.replace('-', '')

    if ',' in s:
        return datetime.strptime(''.join(s.split()[1:4]), '%d%b%Y')

    if 'T' in s:
        s = s[:s.index('T')]

    return datetime.strptime(s, '%Y%m%d')


def date_to_str(date):
    """Takes attribute in datetime format.
    Changes date into string of %Y-%m-%d format"""
    logging.info('Running date_to_str() function from utils.py.')

    assert(isinstance(date, datetime))
    return datetime.strftime(date, '%Y-%m-%d')


def open_console():
    """Opens console"""
    logging.info('Running open_console() function from utils.py.')
    return sys.stdout


def close_console(console):
    """Closes console"""
    logging.info('Running close_console() function from utils.py.')
    if console is not sys.stdout:
        console.close


class Console:
    """Ensures that file will be closed after writing."""
    def __enter__(self):
        self._console = open_console()
        return self

    def __exit__(self, *args):
        close_console(self._console)

    def write(self, s):
        logging.info('Running write() function from utils.py. Class Console.')
        self._console.write(s)


class NewsEncoder(json.JSONEncoder):
    """Encodes json object into dict."""
    def default(self, obj):
        logging.info('Running default() function from utils.py.\
                     Class NewsEncoder(json.JSONEncoder).')
        if isinstance(obj, RssItem):
            return {'title': obj.title, 'date': date_to_str(obj.date),
                    'link': (obj.link)}

        return json.JSONEncoder.default(self, obj)
