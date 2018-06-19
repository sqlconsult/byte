#!/usr/bin/env python3

import unittest
# from unittest.mock import patch
import candy


# inherit unittest TestCase for asserts
class TestCandy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # run once before a single test case runs
        # name is case sensitive
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        # run once after all test cases run
        # name is case sensitive
        print('tearDownClass')

    def setUp(self):
        # run before each and every test case runs
        print('setUp')

    def tearDown(self):
        # run after each and every test case runs
        print('tearDown')

    def test_bonus_candy(self):
        print('test_bonus_candy')
        #
        # dark       --> 1 dark
        # milk       --> 1 milk + 1 sugar free
        # sugar free --> 1 dark + 1 sugar_free
        # white      --> 1 sugar free + 1 white
        #
        bonus = {'dark': {'dark': 1, 'milk': 0, 'sugar_free': 0, 'white': 0},
                 'milk': {'dark': 0, 'milk': 1, 'sugar_free': 1, 'white': 0},
                 'sugar free': {'dark': 1, 'milk': 0, 'sugar_free': 1, 'white': 0},
                 'white': {'dark': 0, 'milk': 0, 'sugar_free': 1, 'white': 1},
                 'unknown': {'dark': 0, 'milk': 0, 'sugar_free': 0, 'white': 0}}

        for key, value in bonus.items():
            dark, milk, sugar_free, white = candy.bonus_candy(key)
            self.assertEqual(dark, value['dark'])
            self.assertEqual(milk, value['milk'])
            self.assertEqual(sugar_free, value['sugar_free'])
            self.assertEqual(white,  value['white'])

    def test_candy_math(self):
        result = candy.candy_math(14, 2, 6, 'milk')
        self.assertEqual(result['dark'], 0)
        self.assertEqual(result['milk'], 8)
        self.assertEqual(result['sugar free'], 1)
        self.assertEqual(result['white'], 0)

        result = candy.candy_math(12, 2, 5, 'milk')
        self.assertEqual(result['dark'], 0)
        self.assertEqual(result['milk'], 7)
        self.assertEqual(result['sugar free'], 1)
        self.assertEqual(result['white'], 0)

        result = candy.candy_math(12, 4, 4, 'dark')
        self.assertEqual(result['dark'], 3)
        self.assertEqual(result['milk'], 0)
        self.assertEqual(result['sugar free'], 0)
        self.assertEqual(result['white'], 0)


if __name__ == '__main__':
    unittest.main()
