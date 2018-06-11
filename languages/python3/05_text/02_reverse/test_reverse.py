import unittest

from reverse import reverse

class TestReverse(unittest.TestCase):

    def assert_reverse(self, a, b):
        self.assertEqual(reverse(a), b)

    def test_a(self):
        self.assert_reverse('a', 'a')

    def test_foobar(self):
        self.assert_reverse('foobar', 'raboof')

    def test_racecar(self):
        self.assert_reverse('racecar', 'racecar')

    def test_alphabet(self):
        self.assert_reverse('abcdefghijklmnopqrstuvwxyz',
                            'zyxwvutsrqponmlkjihgfedcba')
