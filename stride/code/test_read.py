#!/usr/bin/env python3

import os
import pytest

import constants as constants
import controller as controller
import model as model
import order as order


def test_controller_read_order_file():
    #
    # test successful read file
    #
    input_file_name = os.path.join('../input', 'orders.csv')
    valid_orders, invalid_orders, read_successful = controller.read_order_file(input_file_name)
    assert len(valid_orders) == 4
    assert len(invalid_orders) == 0
    assert read_successful
    #
    # test missing file exception is handled
    #
    input_file_name = '../input/orders_xxx.csv'
    valid_orders, invalid_orders, read_successful = controller.read_order_file(input_file_name)
    assert len(valid_orders) == 0
    assert len(invalid_orders) == 0
    assert not read_successful
    #
    # test zero length file exception is handled
    #
    input_file_name = 'file_size_zero.txt'
    os.system('touch {0}'.format(input_file_name))
    os.truncate(input_file_name, 0)
    valid_orders, invalid_orders, read_successful = controller.read_order_file(input_file_name)
    assert len(valid_orders) == 0
    assert len(invalid_orders) == 0
    assert not read_successful
    os.system('rm {0}'.format(input_file_name))


def test_model_read_file():
    #
    # test successful read file
    #
    input_file_name = os.path.join('../input', 'orders.csv')
    valid_orders, invalid_orders = model.read_file(input_file_name)
    assert len(valid_orders) == 4
    assert len(invalid_orders) == 0
    #
    # test missing file exception is raised
    #
    input_file_name = os.path.join('../input', 'orders_xxx.csv')
    pytest.raises(FileNotFoundError, model.read_file, input_file_name)
    #
    # test zero length file exception is raised
    #
    input_file_name = 'file_size_zero.txt'
    os.system('touch {0}'.format(input_file_name))
    os.truncate(input_file_name, 0)
    pytest.raises(StopIteration, model.read_file, input_file_name)
    os.system('rm {0}'.format(input_file_name))


def test_model_validate_input_order():
    #
    # test valid input file
    #
    line_num = 1
    line = '12,2,5,"milk"\n'
    valid_test_order = order.InputOrder(line_num, line)
    valid_order = model.validate_input_order(valid_test_order)
    assert type(valid_order).__name__ == 'ValidOrder'
    assert valid_order.__sizeof__() == 32
    #
    # test invalid data is correctly caught
    #
    line_num = 1
    line = 'a,b,c,"d"\n'
    invalid_test_order = order.InputOrder(line_num, line)
    invalid_order = model.validate_input_order(invalid_test_order)
    assert type(invalid_order).__name__ == 'InvalidOrder'
    assert invalid_order.__sizeof__() == 32

    # Four errors
    assert len(invalid_order.errors) == 4

    assert invalid_order.errors[0] == 'Invalid cash amount [a]'
    assert invalid_order.errors[1] == 'Invalid price [b]'
    assert invalid_order.errors[2] == 'Invalid wrappers [c]'
    assert invalid_order.errors[3] == 'Invalid candy type [d]'


def test_order_input_order():
    #
    # test input line is correctly parsed
    #
    line_num = 1
    line = '12,2,5,"milk"\n'
    imported_order = order.InputOrder(line_num, line)
    assert imported_order.line == line
    assert imported_order.line_num == line_num
    assert imported_order.cash_avail == '12'
    assert imported_order.price == '2'
    assert imported_order.wrappers_needed == '5'
    assert imported_order.candy_type == constants.MILK
