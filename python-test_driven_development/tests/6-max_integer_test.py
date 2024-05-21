#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer()"""


    def test_1_max_liste_int(self):
        self.assertTrue(max_integer([3, 6]) == 6)
        self.assertTrue(max_integer([-1, -43]) == -1)
        self.assertTrue(max_integer([35]) == 35)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertTrue(max_integer([1, 2, float('inf')]) == float('inf'))

    def test_2_max_liste_int_float(self):
        self.assertTrue(max_integer((5.2, 10.2, 1)) == 10.2)

    def test_3_Liste_of_strings(self):
        self.assertTrue(max_integer(["b", "a", "ba", "aaa"]) == "ba")

    def test_4_max_liste_of_tuple(self):
        self.assertTrue(max_integer([(1, 3), (1, 2, 1)]) == (1, 3))
