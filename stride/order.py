#!/usr/bin/env python3


class InputOrder:
    """Class to hold single order"""
    def __init__(self, cash_avail, price, wrappers_needed, candy_type):
        self.cash_avail = cash_avail
        self.price = price
        self.wrappers_needed = wrappers_needed
        self.candy_type = candy_type


class Order:
    """Class to hold single order"""
    def __init__(self, cash_avail, price, wrappers_needed, candy_type):
        self.cash_avail = int(cash_avail)
        self.price = int(price)
        self.wrappers_needed = int(wrappers_needed)
        self.candy_type = candy_type
