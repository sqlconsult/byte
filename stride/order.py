#!/usr/bin/env python3


class InputOrder:
    """Class to hold single order"""
    def __init__(self, line_num, line):
        self.line_num = line_num
        self.line = line

        # parse input line
        flds = line.split(',')
        self.cash_avail = flds[0]
        self.price = flds[1]
        self.wrappers_needed = flds[2]
        # clean candy type (remove double quotes and trailing new line)
        candy_tmp = flds[3].lower().replace('\"', '')  # remove double quotes
        inp_candy_type = candy_tmp[:-1]                # remove trailing newline  "\n"
        self.candy_type = inp_candy_type


class Order:
    """Class to hold single order"""
    def __init__(self, line_num, cash_avail, price, wrappers_needed, candy_type):
        self.line_num = line_num
        self.cash_avail = int(cash_avail)
        self.price = int(price)
        self.wrappers_needed = int(wrappers_needed)
        self.candy_type = candy_type
