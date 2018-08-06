import unittest
import json
from loader import loader

class Loader_Test(unittest.TestCase):
	
	def test_loader(self):
		filename = "./Challenge/input.txt"
		loader(filename)
		with open('./Challenge/output.txt') as output:
			expected = output.readlines()
		with open('result.txt') as f:
			result = f.readlines()

		for i in range(len(expected)):
			expected_data = json.loads(expected[i])
			result_data = json.loads(result[i])
			self.assertEqual(expected_data["id"], result_data["id"])
			self.assertEqual(expected_data["accepted"], result_data["accepted"])
			self.assertEqual(expected_data["customer_id"], result_data["customer_id"])


if __name__ == '__main__':
	unittest.main()
