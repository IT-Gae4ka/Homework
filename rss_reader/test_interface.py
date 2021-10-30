import argparse
import logging
from datetime import datetime
import unittest
from interface import create_parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()

    def test_source(self):
        parsed = self.parser.parse_args(['https://news.yahoo.com/rss/'])
        self.assertEqual(parsed.source, 'https://news.yahoo.com/rss/')

    def test_json(self):
        parsed = self.parser.parse_args(['--json', '--json'])
        self.assertEqual(type(parsed.json), bool)

    def test_limit(self):
        limit = 5
        parsed = self.parser.parse_args(['--limit', str(limit)])
        self.assertEqual(parsed.limit, limit)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
