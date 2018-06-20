#!/usr/bin/env python3

from order import InputOrder, Order
from input_errors import InputError


def is_number(s, typ):
    """
    :param s:   String to check
    :param typ: Numeric type ( 'float' | 'int' }
    :return:    Returns True is s is a number, else False
    """
    try:
        if typ == 'float':
            float(s)
        elif typ == 'int':
            int(s)
        return True
    except ValueError:
        return False


def read_file(file_path):
    """
    :param file_path: Path to order file to read
    :return: Dictionary of Input_Orders (strings) from input file
    """
    # initialize return list
    imported_orders = []

    try:
        # read input file
        with open(file_path) as f:
            # skip header
            next(f)

            # process 1 line at time
            for line_num, line in enumerate(f):
                imported_order = InputOrder(line_num, line)
                imported_orders.append(imported_order)

        return 0, imported_orders, 0

    except EOFError as ex:
        return 1, imported_orders, ex

    except FileNotFoundError as ex:
        return 2, imported_orders, ex

    except StopIteration as ex:
        return 3, imported_orders, ex


def validate_input_data(inp_orders):
    """
    :param inp_orders: Dictionary of input lines
    :return: 2 dictionaries - 1: valid input lines - dictionary of Orders (key = line number)
                              2: invalid input lines - dictionary of Input_Errors (key = line number)
    """
    # initialize return value dictionaries
    valid_lines = []
    invalid_lines = []

    try:
        # loop over all input lines
        for inp_order in inp_orders:
            line_num = inp_order.line_num
            line = inp_order.line
            inp_cash = inp_order.cash_avail
            inp_price = inp_order.price
            inp_wrappers = inp_order.wrappers_needed
            candy_type = inp_order.candy_type

            err_msgs = []

            valid = True
            if not is_number(inp_cash, 'int'):
                msg = 'Invalid cash amount [{cash}]'.format(cash=inp_cash)
                err_msgs.append(msg)
                valid = False

            if not is_number(inp_price, 'int'):
                msg = 'Invalid price [{price}]'.format(price=inp_price)
                err_msgs.append(msg)
                valid = False

            if not is_number(inp_wrappers, 'int'):
                msg = 'Invalid wrappers [{wrappers}]'.format(wrappers=inp_wrappers)
                err_msgs.append(msg)
                valid = False

            if candy_type not in ['milk', 'white', 'sugar free', 'dark']:
                msg = 'Invalid candy type [{candy_type}]'.format(candy_type=candy_type)
                err_msgs.append(msg)
                valid = False

            if valid:
                if line_num not in valid_lines:
                    tmp_order = Order(line_num,
                                      int(inp_cash),
                                      int(inp_price),
                                      int(inp_wrappers),
                                      candy_type)
                    valid_lines.append(tmp_order)
            else:
                tmp_err = InputError(line_num, line, err_msgs)
                invalid_lines.append(tmp_err)

        return valid_lines, invalid_lines, 0, 0

    except RuntimeError as ex:
        return valid_lines, invalid_lines, -1, ex


def write_redemptions(redemptions_to_write, file_path):
    """
    :param redemptions_to_write: dictionary of wrappers to write
    :param file_path:            path to output file
    :return:                     error code, exception or 0

    error code: 0 = No error, -1 = EOFError, -2 = FileNotFoundError, -3 = RuntimeError
    """
    # initialize number of record written
    write_cnt = 0

    # output line template format
    line_to_write_fmt = 'milk {milk},dark {dark},white {white},sugar free {sugar_free}'

    # open output file
    with open(file_path, 'w+') as g:
        # loop over each set of wrappers and write to output file
        for redemption in redemptions_to_write:
            output_line = line_to_write_fmt.format(milk=redemption['milk'],
                                                   dark=redemption['dark'],
                                                   white=redemption['white'],
                                                   sugar_free=redemption['sugar_free'])
            g.write(output_line)
            # increment records written counter
            write_cnt += 1

    # return error code = 0, success status, no exception
    return 0, write_cnt, 0

