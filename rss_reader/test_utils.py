from .import utils
import unittest
from datetime import datetime

class Test_utils(unittest.TestCase):
	def test_date_to_str(self):
		self.assertEqual(utils.date_to_str(datetime(2021, 12, 11)), '2021-12-11')
		self.assertEqual(utils.date_to_str(datetime(2020, 9, 22)), '2020-09-22')

	def test_date_from_str(self):
		self.assertEqual(datetime(2021, 12, 11), utils.date_from_str('20211211'))
		self.assertEqual(datetime(2020, 9, 22), utils.date_from_str('20200922'))
		self.assertEqual(datetime(2021, 12, 11), utils.date_from_str('2021-12-11'))
		self.assertEqual(datetime(2020, 9, 22), utils.date_from_str('2020-09-22'))
		self.assertEqual(datetime(2021, 10, 30).date(),
			utils.date_from_str('Sat, 30 Oct 2021 10:25:26 -0400').date())

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
