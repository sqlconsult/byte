#!/usr/bin/env python3


def read_input_file(file_path):
    """
    :param file_path: path to input file to read
    :return:          list of lines read
    """
    with open(file_path) as f:
        lines = f.readlines()

    # remove \n from input lines
    content = [x.strip() for x in lines]
    return content
