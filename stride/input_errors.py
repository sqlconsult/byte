#!/usr/bin/env python3


class InputError:
    def __init__(self, line_num, line, errors):
        self.line_num = line_num
        self.line = line
        self.errors = errors
