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
        print('TestCandy: setUpClass')

    @classmethod
    def tearDownClass(cls):
        # run once after all test cases run
        # name is case sensitive
        print('TestCandy: tearDownClass')

    def setUp(self):
        # run before each and every test case runs
        print('TestCandy: setUp')

    def tearDown(self):
        # run after each and every test case runs
        print('TestCandy: tearDown')

    def test_bonus_candy(self):
        print('TestCandy: test_bonus_candy')
        #
        # dark       --> 1 dark
        # milk       --> 1 milk + 1 sugar free
        # sugar free --> 1 dark + 1 candy.SUGAR_FREE
        # candy.WHITE      --> 1 sugar free + 1 candy.WHITE
        #
        bonus = {candy.DARK: {candy.DARK: 1, candy.MILK: 0, candy.SUGAR_FREE: 0, candy.WHITE: 0},
                 candy.MILK: {candy.DARK: 0, candy.MILK: 1, candy.SUGAR_FREE: 1, candy.WHITE: 0},
                 candy.SUGAR_FREE: {candy.DARK: 1, candy.MILK: 0, candy.SUGAR_FREE: 1, candy.WHITE: 0},
                 candy.WHITE: {candy.DARK: 0, candy.MILK: 0, candy.SUGAR_FREE: 1, candy.WHITE: 1},
                 'unknown': {candy.DARK: 0, candy.MILK: 0, candy.SUGAR_FREE: 0, candy.WHITE: 0}}

        for key, value in bonus.items():
            dark, milk, sugar_free, white = candy.bonus_candy(key)
            self.assertEqual(dark, value[candy.DARK])
            self.assertEqual(milk, value[candy.MILK])
            self.assertEqual(sugar_free, value[candy.SUGAR_FREE])
            self.assertEqual(white,  value[candy.WHITE])

    def test_candy_math(self):
        result = candy.candy_math(14, 2, 6, candy.MILK)
        self.assertEqual(result[candy.DARK], 0)
        self.assertEqual(result[candy.MILK], 8)
        self.assertEqual(result[candy.SUGAR_FREE], 1)
        self.assertEqual(result[candy.WHITE], 0)

        result = candy.candy_math(12, 2, 5, candy.MILK)
        self.assertEqual(result[candy.DARK], 0)
        self.assertEqual(result[candy.MILK], 7)
        self.assertEqual(result[candy.SUGAR_FREE], 1)
        self.assertEqual(result[candy.WHITE], 0)

        result = candy.candy_math(12, 4, 4, candy.DARK)
        self.assertEqual(result[candy.DARK], 3)
        self.assertEqual(result[candy.MILK], 0)
        self.assertEqual(result[candy.SUGAR_FREE], 0)
        self.assertEqual(result[candy.WHITE], 0)


if __name__ == '__main__':
    unittest.main()
