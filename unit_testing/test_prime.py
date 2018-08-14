import unittest
from primes import *


def generate_tests():
	return [11, 3, 17, 23]

class PrimeTest(unittest.TestCase):

	def test_hello(self):
		for i in generate_tests():
			self.assertEqual(prime(i), True)


if __name__ == "__main__":
	unittest.main()