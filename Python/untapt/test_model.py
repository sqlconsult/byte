#!/usr/bin/env python3

import os
import unittest
import model


# inherit unittest TestCase for asserts
class TestModel(unittest.TestCase):

    def test_model_read_file(self):
        #
        # test successful read file
        #
        print('==> test_model_read_file: test #1')
        input_file_name = 'input.txt'
        lines = model.read_input_file(input_file_name)
        self.assertEqual(len(lines), 5)
        #
        # test missing file exception is raised
        #
        print('==> test_model_read_file: test #2')
        input_file_name = 'input_xxx.csv'
        self.assertRaises(FileNotFoundError, model.read_input_file, input_file_name)
        #
        # test zero length file exception is not raised
        #
        print('==> test_model_read_file: test #3')
        input_file_name = 'file_size_zero.txt'
        os.system('touch {0}'.format(input_file_name))
        os.truncate(input_file_name, 0)
        lines = model.read_input_file(input_file_name)
        self.assertEqual(len(lines), 0)
        os.system('rm {0}'.format(input_file_name))


if __name__ == '__main__':
    unittest.main()
