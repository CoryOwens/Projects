#!/usr/bin/python3
import unittest

from prime_factors import prime_factor_brute


class PrimeFactorsBaseTest(object):
    factor_map = {
        1: [],
        2: [2],
        3: [3],
        4: [2, 2],
        5: [5],
        6: [2, 3],
        7: [7],
        8: [2, 2, 2],
        9: [3, 3],
        100: [2, 2, 5, 5],
        455: [5, 7, 13],
        595: [5, 7, 17],
        4181: [37, 113],
        65786133: [3, 7, 449, 6977],
        6771850660326771845760143243106604010453055227730524202299702024885329824963100768890085276675574734: [
            2, 31, 61, 15511, 1690781263,
            68274514930886057056995204959000330017607041291842458014796040739802561578355840309
        ],
        10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376: [2]*1000
    }

    def assert_prime_factor(self, x, factors):
        actual = self.prime_factor(x)
        self.assertEqual(factors, actual, 'Factors of {}, expected {}, got {}'
                         .format(x, factors, actual))


for x, factors in PrimeFactorsBaseTest.factor_map.items():
    func_name = 'test_prime_factor_{}'.format(x)

    def func(self):
        self.assert_prime_factor(x, factors)
    setattr(PrimeFactorsBaseTest, func_name, func)


class PrimeFactorsTest(PrimeFactorsBaseTest, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.prime_factor = staticmethod(prime_factor_brute)


if __name__ == '__main__':
    unittest.main()
