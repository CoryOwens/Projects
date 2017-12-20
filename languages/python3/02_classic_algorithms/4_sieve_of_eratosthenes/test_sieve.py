#!/usr/bin/python3
import unittest
from sieve import sieve


class TestSieve(unittest.TestCase):

	def test_sieve_0(self):
		with self.assertRaises(ValueError):
			sieve(0)

	def test_sieve_1(self):
		with self.assertRaises(ValueError):
			sieve(1)

	def test_sieve_2(self):
		expected = [2]
		actual = sieve(2)
		self.assertEqual(expected, actual)

	def test_sieve_10(self):
		expected = [2, 3, 5, 7]
		actual = sieve(10)
		self.assertEqual(expected, actual)

	def test_sieve_200(self):
		expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
		actual = sieve(200)
		self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
