import unittest
from vlc_date import Date

class Date_Test(unittest.TestCase):

	def test_is_different_date(self):
		date1 = Date(2018, 8, 5)
		date2 = Date(2018, 8, 6)
		result1 = date1.is_different_date(date2)
		self.assertIs(result1, True)

		date3 = Date(2018, 7, 20)
		date4 = Date(2018, 7, 20)
		result2 = date3.is_different_date(date4)
		self.assertIs(result2, False)

	def test_is_different_week(self):
		date1 = Date(2018, 8, 5)
		date2 = Date(2018, 8, 6)
		result1 = date1.is_different_week(date2)
		self.assertIs(result1, True)

		date3 = Date(2018, 8, 3)
		date4 = Date(2018, 8, 5)
		result2 = date3.is_different_week(date4)
		self.assertIs(result2, False)

		date5 = Date(2018, 8, 2)
		date6 = Date(2018, 8, 9)
		result3 = date5.is_different_week(date6)
		self.assertIs(result3, True)

if __name__ == '__main__':
    unittest.main()
