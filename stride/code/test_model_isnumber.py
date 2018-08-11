#!/usr/bin/env python3

import model as model


def test_int():
    """
    Tests string to integer conversion method
    :return:
    """
    valid = model.is_number('123', 'int')
    invalid = model.is_number('abc', 'int')
    assert valid
    assert not invalid


def test_float():
    """
    Tests string to float conversion method
    :return:
    """
    valid = model.is_number('12.3', 'float')
    invalid = model.is_number('abc', 'float')
    assert valid
    assert not invalid


def test_invalid_type():
    """
    Tests invalid type converions fail
    :return:
    """
    invalid = model.is_number(123, 'int_xxx')
    assert not invalid

    invalid = model.is_number(12.3, 'float_xxx')
    assert not invalid
