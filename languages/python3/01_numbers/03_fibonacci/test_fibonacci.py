#!/usr/bin/python3
import unittest
from fibonacci import fibonacci_recursive, fibonacci_iterative, fibonacci_doubling

class TestFibonacciBase(object):

	def assert_fibonacci(self, n, exp):
		self.assertEqual(exp, self.fibonacci(n))
	
	def test_fibonacci_negative(self):
		with self.assertRaises(ValueError):
			self.fibonacci(-1)

	def test_fibonacci_0(self):
		self.assert_fibonacci(0, 0)

	def test_fibonacci_1(self):
		self.assert_fibonacci(1, 1)

	def test_fibonacci_2(self):
		self.assert_fibonacci(2, 1)

	def test_fibonacci_3(self):
		self.assert_fibonacci(3, 2)

	def test_fibonacci_4(self):
		self.assert_fibonacci(4, 3)

	def test_fibonacci_5(self):
		self.assert_fibonacci(5, 5)

	def test_fibonacci_6(self):
		self.assert_fibonacci(6, 8)

	def test_fibonacci_1000(self):
		self.assert_fibonacci(1000, 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)
		
class TestFibonacciRecursive(TestFibonacciBase, unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.fibonacci = staticmethod(fibonacci_recursive)

	def test_fibonacci_1000(self):
		with self.assertRaises(RuntimeError):
			self.fibonacci(1000)  # exceeds maximum recursion depth

class TestFibonacciIterative(TestFibonacciBase, unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.fibonacci = staticmethod(fibonacci_iterative)

class TestFibonacciDoubling(TestFibonacciBase, unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.fibonacci = staticmethod(fibonacci_doubling)

if __name__ == '__main__':

    unittest.main()
