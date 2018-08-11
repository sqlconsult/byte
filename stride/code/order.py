#!/usr/bin/env python3


class InputOrder:
    """Class to hold single order from input file"""
    def __init__(self, line_num, line):
        self.line_num = line_num
        self.line = line

        # parse input line
        # sample input line: '6,2,2,"white"\n'
        flds = line.split(',')
        self.cash_avail = flds[0].strip()
        self.price = flds[1].strip()
        self.wrappers_needed = flds[2].strip()
        # clean candy type (remove double quotes and trailing new line)
        self.candy_type = flds[3].lower().strip().replace('\"', '')  # remove double quotes


class ValidOrder:
    """Class to hold single valid order"""
    def __init__(self, line_num=None, cash_avail=None, price=None, wrappers_needed=None, candy_type=None):
        self.line_num = line_num
        self.cash_avail = int(cash_avail)
        self.price = int(price)
        self.wrappers_needed = int(wrappers_needed)
        self.candy_type = candy_type


class InvalidOrder:
    """Class to hold single invalid order"""
    def __init__(self, line_num=None, line=None, errors=None):
        self.line_num = line_num
        self.line = line
        self.errors = errors
