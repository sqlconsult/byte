#!/usr/bin/env python3

import os
import unittest
from unittest.mock import patch
from order import InputOrder
import model


# inherit unittest TestCase for asserts
class TestRead(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # run once before a single test case runs
        # name is case sensitive
        print('TestRead: setUpClass')

    @classmethod
    def tearDownClass(cls):
        # run once after all test cases run
        # name is case sensitive
        print('TestRead: tearDownClass')

    def setUp(self):
        # run before each and every test case runs
        print('TestRead: setUp')
        #
        # read input file into dictionary of InputOrders
        #
        self.file_nm = os.path.join('input', 'orders.csv')
        self.read_status, self.inp_orders, self.read_exception = model.read_file(self.file_nm)

    def tearDown(self):
        # run after each and every test case runs
        print('TestRead: tearDown')

    def test_read_file(self):
        print('TestRead: test_read_file')
        #
        # test successful read file
        #
        self.assertEqual(self.read_status, 0)
        self.assertEqual(len(self.inp_orders), 4)
        self.assertEqual(self.read_exception, 0)
        #
        # test missing file
        #
        self.file_nm = 'input/orders_xxx.csv'
        self.read_status, self.inp_orders, self.read_exception = model.read_file(self.file_nm)
        self.assertEqual(self.read_status, 2)
        self.assertEqual(len(self.inp_orders), 0)
        self.assertEqual(self.read_exception.args[0], 2)
        self.assertEqual(self.read_exception.args[1], 'No such file or directory')

    def test_read_error(self):
        print('TestRead: test_read_error')
        file_nm = 'file_size_zero.txt'
        os.system('touch {0}'.format(file_nm))
        os.truncate(file_nm, 0)
        read_status, inp_orders, read_exception = model.read_file(file_nm)

        self.assertEqual(read_status, 3)
        self.assertEqual(len(inp_orders), 0)
        os.system('rm {0}'.format(file_nm))

    def test_validate_file(self):
        print('TestRead: test_validate_file')
        #
        # test valid input file
        #
        valid_orders, invalid_orders, validate_status, valid_exception = \
            model.validate_input_data(self.inp_orders)

        self.assertEqual(len(valid_orders), 4)
        self.assertEqual(len(invalid_orders), 0)
        self.assertEqual(validate_status, 0)
        self.assertEqual(valid_exception, 0)
        #
        # these tests test invalid data is correctly caught
        #
        fail_orders = [InputOrder(1, 'a,b,c,d\n')]
        valid_orders, invalid_orders, validate_status, valid_exception = \
            model.validate_input_data(fail_orders)
        # No valid orders
        self.assertEqual(len(valid_orders), 0)
        # One invalid order
        self.assertEqual(len(invalid_orders), 1)
        # Status == 0 (success)
        self.assertEqual(validate_status, 0)
        # Four errors
        self.assertEqual(len(invalid_orders[0].errors), 4)

        self.assertEqual(invalid_orders[0].errors[0], 'Invalid cash amount [a]')
        self.assertEqual(invalid_orders[0].errors[1], 'Invalid price [b]')
        self.assertEqual(invalid_orders[0].errors[2], 'Invalid wrappers [c]')
        self.assertEqual(invalid_orders[0].errors[3], 'Invalid candy type [d]')


if __name__ == '__main__':
    unittest.main()
