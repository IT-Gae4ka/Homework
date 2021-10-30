from .rss_item import RssItem
import utils
from abc import ABCMeta, abstractmethod
import csv
import logging
import unittest
from io import StringIO
import sys
from unittest import mock
from datetime import datetime
from .writers import CacheWriter, JsonWriter, Console

news = [RssItem('Employee who killed gunman likely saved lives, police say', datetime(2021, 10, 22), 'https://news.yahoo.com/employee-killed-gunman-likely-saved-211530368.html'),
        RssItem('A 55-year-old mother of 9 was sentenced to death by hanging over possessing around 4 ounces of meth',
                datetime(2021, 10, 23), 'https://news.yahoo.com/55-old-mother-9-sentenced-054433946.html')]

class Test_CacheWriter(unittest.TestCase):

    @mock.patch("utils.open_cache_file_for_write")
    def test_write(self, f):
        cache_file = StringIO()
        cache_file.close = lambda self: None
        f.return_value = cache_file
        writer = CacheWriter()
        writer.write(news)
        print('contents', cache_file.getvalue())
        csv_news = list(csv.reader(cache_file, delimiter=','))

        self.assertEqual(len(csv_news), 2)
        self.assertEqual(csv_news[0][0], 'Employee who killed gunman likely saved lives, police say')
        self.assertEqual(csv_news[0][1], '20211022')
        self.assertEqual(csv_news[0][2], 'https://news.yahoo.com/employee-killed-gunman-likely-saved-211530368.html')

        self.assertEqual(csv_news[1][0], 'A 55-year-old mother of 9 was sentenced to death by hanging over possessing around 4 ounces of meth')
        self.assertEqual(csv_news[1][1], '20211023')
        self.assertEqual(csv_news[1][2], 'https://news.yahoo.com/55-old-mother-9-sentenced-054433946.html')

    

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    