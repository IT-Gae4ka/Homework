from .rss_item import RssItem
from .utils import Console, date_to_str, NewsEncoder, open_cache_file_for_write
from abc import ABCMeta, abstractmethod
import csv
import logging
import unittest
from io import StringIO
import sys
import mocker
from datetime import datetime

news = "Employee who killed gunman likely saved lives, police say,\
		20211022,\
		https://news.yahoo.com/employee-killed-gunman-likely-saved-211530368.html\
		A 55-year-old mother of 9 was sentenced to death by hanging over possessing around 4 ounces of meth,\
		20211022,\
		https://news.yahoo.com/55-old-mother-9-sentenced-054433946.html\
		Every Day, Biden Smells Like More of a Loser,\
		20211023,\
		https://news.yahoo.com/every-day-biden-smells-more-033653915.html"

class Test_CacheWriter(unittest.TestCase):

	@mock.patch("utils.open_cache_file_for_write")
	def test_write(self, cache_file):
		cache_file = StringIO()
		cache_file.close = lambda self: None
		cache_file.return_value = cache_file
		storage = rss_storage.RssStorage(
		self.assertEqual()

	

if __name__ == "__main__":
	unittest.main(argv=['first-arg-is-ignored'], exit=False)
	