import unittest

from coin_flip import coin_flip


class TestCoinFlip(unittest.TestCase):

    def assert_h_or_t(self, flips):
        for f in flips:
            self.assertIn(f, ['H', 'T'])

    def test_bunch(self):
        for i in range(100):
            flips = coin_flip(i)
            self.assertEqual(i, len(flips))
            self.assert_h_or_t(flips)

    def test_probability(self):
        for i in range(10):
            n = 100000
            flips = coin_flip(n)
            self.assertEqual(n, len(flips))
            self.assert_h_or_t(flips)
            h = flips.count('H')
            percent = h/n
            self.assertAlmostEqual(0.50, percent, 2)

    def test_nondeterministic(self):
        for i in range(10):
            n = 100000
            flips_a = coin_flip(n)
            self.assertEqual(n, len(flips_a))
            self.assert_h_or_t(flips_a)
            flips_b = coin_flip(n)
            self.assertEqual(n, len(flips_b))
            self.assert_h_or_t(flips_b)
            self.assertNotEqual(flips_a, flips_b)
