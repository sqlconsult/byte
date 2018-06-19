#!/usr/bin/env python3

import unittest.mock
import unittest
import model


# inherit unittest TestCase for asserts
class TestWrite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # run once before a single test case runs
        # name is case sensitive
        print('TestWrite: setUpClass')

    @classmethod
    def tearDownClass(cls):
        # run once after all test cases run
        # name is case sensitive
        print('TestWrite: tearDownClass')

    def setUp(self):
        # run before each and every test case runs
        print('TestWrite: setUp')

    def tearDown(self):
        # run after each and every test case runs
        print('TestWrite: tearDown')

    def test_write_file(self):
        #
        # test file exists write
        #
        output_file_name = 'output/redemptions.csv'
        r1 = {'milk': 1, 'dark': 2, 'white': 3, 'sugar_free': 4}
        r2 = {'milk': 11, 'dark': 22, 'white': 33, 'sugar_free': 44}
        r3 = {'milk': 111, 'dark': 222, 'white': 333, 'sugar_free': 444}
        r4 = {'milk': 1111, 'dark': 2222, 'white': 3333, 'sugar_free': 4444}
        redemptions_to_write = [r1, r2, r3, r4]

        write_error_code, write_cnt, write_exception = \
            model.write_redemptions(redemptions_to_write, output_file_name)

        self.assertEqual(write_error_code, 0)
        self.assertEqual(write_exception, 0)
        self.assertEqual(write_cnt, 4)
        #
        # test file does not exist write
        #
        output_file_name = 'output/redemptions_xxx.csv'
        redemptions_to_write = [r1, r2, r3, r4]

        write_error_code, write_cnt, write_exception = \
            model.write_redemptions(redemptions_to_write, output_file_name)

        self.assertEqual(write_error_code, 0)
        self.assertEqual(write_exception, 0)
        self.assertEqual(write_cnt, 4)

    def test_wite_error(self):
        pass


if __name__ == '__main__':
    unittest.main()