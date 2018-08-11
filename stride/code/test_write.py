#!/usr/bin/env python3
import os

import constants as constants
import controller as controller
import model as model


def test_controller_write_file():
    #
    # test file exists write
    #
    file_dir = '../output'
    file_nm = 'test_controller_output.csv'
    output_file_name = os.path.join(file_dir, file_nm)
    r1 = {constants.MILK: 1, constants.DARK: 2, constants.WHITE: 3, constants.SUGAR_FREE: 4}
    r2 = {constants.MILK: 11, constants.DARK: 22, constants.WHITE: 33, constants.SUGAR_FREE: 44}
    r3 = {constants.MILK: 111, constants.DARK: 222, constants.WHITE: 333, constants.SUGAR_FREE: 444}
    r4 = {constants.MILK: 1111, constants.DARK: 2222, constants.WHITE: 3333, constants.SUGAR_FREE: 4444}
    orders_to_write = [r1, r2, r3, r4]

    written_order_cnt = controller.write_output_orders_file(orders_to_write, output_file_name)
    #
    # 1 - test that all 4 orders were written
    #
    assert written_order_cnt == 4
    #
    # 2 - ensure output file exists
    #
    out_file_exists = os.path.isfile(output_file_name)
    assert out_file_exists
    #
    # 3 - check output file contents
    #
    expected_output = ['milk 1,dark 2,white 3,sugar free 4\n',
                       'milk 11,dark 22,white 33,sugar free 44\n',
                       'milk 111,dark 222,white 333,sugar free 444\n',
                       'milk 1111,dark 2222,white 3333,sugar free 4444\n']

    with open(output_file_name, 'r') as f:
        file_content = f.readlines()

    for line_no, line in enumerate(file_content):
        assert line == expected_output[line_no]

    os.system('rm -rf {0}'.format(output_file_name))


def test_model_write_file():
    #
    # test file exists write
    #
    file_dir = '../output'
    file_nm = 'test_model_output.csv'
    output_file_name = os.path.join(file_dir, file_nm)
    r1 = {constants.MILK: 1, constants.DARK: 2, constants.WHITE: 3, constants.SUGAR_FREE: 4}
    r2 = {constants.MILK: 11, constants.DARK: 22, constants.WHITE: 33, constants.SUGAR_FREE: 44}
    r3 = {constants.MILK: 111, constants.DARK: 222, constants.WHITE: 333, constants.SUGAR_FREE: 444}
    r4 = {constants.MILK: 1111, constants.DARK: 2222, constants.WHITE: 3333, constants.SUGAR_FREE: 4444}
    orders_to_write = [r1, r2, r3, r4]

    written_order_cnt = model.write_orders(orders_to_write, output_file_name)
    #
    # 1 - test that all 4 orders were written
    #
    assert written_order_cnt == 4
    #
    # 2 - ensure output file exists
    #
    out_file_exists = os.path.isfile(output_file_name)
    assert out_file_exists
    #
    # 3 - check output file contents
    #
    expected_output = ['milk 1,dark 2,white 3,sugar free 4\n',
                       'milk 11,dark 22,white 33,sugar free 44\n',
                       'milk 111,dark 222,white 333,sugar free 444\n',
                       'milk 1111,dark 2222,white 3333,sugar free 4444\n']

    with open(output_file_name, 'r') as f:
        file_content = f.readlines()

    for line_no, line in enumerate(file_content):
        assert line == expected_output[line_no]

    os.system('rm -rf {0}'.format(output_file_name))
