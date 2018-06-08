#!/usr/bin/python3
import math
import unittest
from copy import deepcopy

from closest_pair import distance, closest_pair_brute, closest_pair_recursive


class TestDistance(unittest.TestCase):

    def assert_distance(self, a, b, expected):
        old_a = deepcopy(a)
        old_b = deepcopy(b)
        self.assertEqual(expected, distance(a, b))
        self.assertEqual(expected, distance(b, a))
        self.assertEqual(expected, distance(tuple([-i for i in a]), tuple([-i for i in b])))
        self.assertEqual(expected, distance(tuple([-i for i in b]), tuple([-i for i in a])))
        self.assertEqual(old_a, a)
        self.assertEqual(old_b, b)

    def test_distance_same(self):
        a = (100, 100)
        b = (100, 100)
        expected = 0
        self.assert_distance(a, b, expected)

    def test_distance_vertical(self):
        a = (0, 100)
        b = (0, 50)
        expected = 50
        self.assert_distance(a, b, expected)

    def test_distance_horizontal(self):
        a = (100, 0)
        b = (50, 0)
        expected = 50
        self.assert_distance(a, b, expected)

    def test_distance_diagonal(self):
        a = (10, 0)
        b = (0, 10)
        expected = 10 * math.sqrt(2)
        self.assert_distance(a, b, expected)

    def test_distance_vertical_negative(self):
        a = (0, 50)
        b = (0, -50)
        expected = 100
        self.assert_distance(a, b, expected)

    def test_distance_horizontal_negative(self):
        a = (50, 0)
        b = (-50, 0)
        expected = 100
        self.assert_distance(a, b, expected)

    def test_distance_diagonal_negative(self):
        a = (10, 10)
        b = (-10, -10)
        expected = 20 * math.sqrt(2)
        self.assert_distance(a, b, expected)

    def test_distance_diagonal_arbitrary(self):
        a =  (-10, 75)
        b = (3, -12)
        expected = math.sqrt(7738)
        self.assert_distance(a, b, expected)


class TestClosestPairBase(object):

    def assert_closest_pair(self, points, expected_a, expected_b):
        old_points = deepcopy(points)
        actual = self.closest_pair(points)
        self.assertEqual(2, len(actual))
        self.assertTrue(expected_a in actual)
        self.assertTrue(expected_b in actual)
        self.assertEqual(old_points, points)

    def test_closest_empty(self):
        with self.assertRaises(ValueError):
            self.closest_pair([])

    def test_closest_single(self):
        with self.assertRaises(ValueError):
            self.closest_pair([(1, 1)])

    def test_closest_two(self):
        a = (0, 0)
        b = (1, 1)
        points = [a, b]
        self.assert_closest_pair(points, a, b)

    def test_closest_three(self):
        a = (0, 0)
        b = (1, 1)
        points = [a, b, (3, 3)]
        self.assert_closest_pair(points, a, b)

    def test_closest_tie(self):
        a = (0, 0)
        b = (1, 1)
        c = (2, 3)
        points = [a, b, c]
        actual = self.closest_pair(points)
        self.assertEqual(2, len(actual))
        # answer could be (a, b) or (b, c), but not (a, c)
        correct = (a in actual and b in actual) or (b in actual and c in actual)
        self.assertTrue(correct)

    def test_closest_arbitrary(self):
        points = [
            (26, -56),
            (-99, -100),
            (-32, 38),
            (-9, 42),
            (-30, -54),
            (20, 6),
            (96, -19),
            (27, -73),
            (-40, -53),
            (76, -42),
        ]
        self.assert_closest_pair(points, points[4], points[8])


class TestClosestPairBrute(TestClosestPairBase, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.closest_pair = staticmethod(closest_pair_brute)


class TestClosestPairRecursive(TestClosestPairBase, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.closest_pair = staticmethod(closest_pair_recursive)



if __name__ == '__main__':
    unittest.main()
