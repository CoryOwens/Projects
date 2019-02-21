#!/usr/bin/python3
import unittest

from pi import pi


class PiBaseTest(object):

    def assert_pi(self, n, exp):
        self.assertEqual(exp, self.pi(n))

    def test_pi_negative(self):
        self.assert_pi(-1, None)

    def test_pi_0(self):
        self.assert_pi(0, None)

    def test_pi_1(self):
        self.assert_pi(1, '3')

    def test_pi_2(self):
        self.assert_pi(2, '3.1')

    def test_pi_3(self):
        self.assert_pi(3, '3.14')

    def test_pi_5(self):
        self.assert_pi(5, '3.1415')

    def test_pi_27(self):
        self.assert_pi(27, '3.14159265358979323846264338')


class PiTest(PiBaseTest, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pi = staticmethod(pi)


if __name__ == '__main__':
    unittest.main()
