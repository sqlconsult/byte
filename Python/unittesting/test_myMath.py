#!/usr/bin/env python3

import unittest
# from unittest.mock import patch
from myMath import MyMath


# inherit unittest TestCase for asserts
class TestMyMath(unittest.TestCase):

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

    def test_myMath(self):
        obj = MyMath()

        print('test integer division')
        result = obj.my_div(4, 2)
        self.assertEqual(result, 2)

        print('test floating point division')
        result = obj.my_div(7, 2)
        self.assertEqual(result, 3.5)

        print('test division by zero')
        # Fails - AssertionError: ZeroDivisionError not raised by my_div
        self.assertRaises(ZeroDivisionError, obj.my_div, 1, 0)

        print('test type error')
        self.assertRaises(TypeError, obj.my_div, '15', 5)

        print('test all other errors')
        # How to test RuntimeError?


if __name__ == '__main__':
    unittest.main()
