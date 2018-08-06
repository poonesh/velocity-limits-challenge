import unittest
from client import Client
from vlc_date import Date

class Client_Test(unittest.TestCase):
    
    # tests for initiate_daily_load method
	def test_initiate_daily_load_same_day(self):
		client = Client(100)
		date1 = Date(2018, 8, 6)
		client.last_load_date = date1
		client.loadamount_currentday = 1000
		client.num_loads_currentday = 1
		load_date = "2018-08-06"
		client.initiate_daily_load(load_date)

		self.assertEqual(client.last_load_date.year, date1.year)
		self.assertEqual(client.last_load_date.month, date1.month)
		self.assertEqual(client.last_load_date.day, date1.day)
		self.assertEqual(client.loadamount_currentday, 1000)
		self.assertEqual(client.num_loads_currentday, 1)


	def test_initiate_daily_load_different_day(self):
		client = Client(100)
		date1 = Date(2018, 8, 6)
		client.last_load_date = date1
		client.loadamount_currentday = 1000
		client.num_loads_currentday = 1
		load_date = "2018-08-07"
		client.initiate_daily_load(load_date)

		self.assertEqual(client.last_load_date.year, 2018)
		self.assertEqual(client.last_load_date.month, 8)
		self.assertEqual(client.last_load_date.day, 7)
		self.assertEqual(client.loadamount_currentday, 0)
		self.assertEqual(client.num_loads_currentday, 0)


	def test_initiate_daily_load_first_time_load(self):
		client = Client(100)
		client.last_load_date = None
		client.loadamount_currentday = 0
		client.num_loads_currentday = 0
		load_date = "2018-08-07"
		client.initiate_daily_load(load_date)

		self.assertEqual(client.last_load_date.year, 2018)
		self.assertEqual(client.last_load_date.month, 8)
		self.assertEqual(client.last_load_date.day, 7)
		self.assertEqual(client.loadamount_currentday, 0)
		self.assertEqual(client.num_loads_currentday, 0)

	# tests for update_daily_load method
	def test_update_daily_load(self):
		client = Client(100)
		load_amount = 2000
		client.update_daily_load(load_amount)

		self.assertEqual(client.loadamount_currentday, 2000)
		self.assertEqual(client.num_loads_currentday, 1)

	# tests for check_daily_load_exceeded method
	def test_daily_load_exceeded_overload(self):
		client = Client(100)
		load_amount = 5005

		self.assertEqual(client.check_daily_load_exceeded(load_amount), True)

	def test_daily_load_exceeded_underload(self):
		client = Client(100)
		load_amount = 4000

		self.assertEqual(client.check_daily_load_exceeded(load_amount), False)

	def test_daily_load_exceeded_over_over_load_capacity(self):
		client = Client(100)
		client.loadamount_currentday = 4000
		client.num_loads_currentday = 1
		load_amount = 1500

		self.assertEqual(client.check_daily_load_exceeded(load_amount), True)

	def test_daily_load_exceeded_over_num_loads(self):
		client = Client(100)
		client.loadamount_currentday = 4000
		client.num_loads_currentday = 4
		load_amount = 1000

		self.assertEqual(client.check_daily_load_exceeded(load_amount), True)




if __name__ == '__main__':
	unittest.main()