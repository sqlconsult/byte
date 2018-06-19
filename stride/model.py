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
    ret_val = {}
    line_num = 0

    try:
        # read input file
        with open(file_path) as f:
            # skip header
            next(f)

            # process 1 line at time
            for line in f:
                # parse input line
                e = line.split(',')
                line_num += 1
                inp_cash = e[0]
                inp_price = e[1]
                inp_wrappers = e[2]
                candy_tmp = e[3].lower().replace('\"', '')  # remove double quotes
                candy_type = candy_tmp[:-1]                 # remove trailing newline  "\n"

                data = InputOrder(inp_cash, inp_price, inp_wrappers, candy_type)
                ret_val[line_num] = data

        return 0, ret_val, 0

    except EOFError as ex:
        return 1, ret_val, ex

    except FileNotFoundError as ex:
        return 2, ret_val, ex

    except RuntimeError as ex:
        return 3, ret_val, ex


def validate_input_data(inp_orders):
    """
    :param inp_orders: Dictionary of input lines
    :return: 2 dictionaries - 1: valid input lines - dictionary of Orders (key = line number)
                              2: invalid input lines - dictionary of Input_Errors (key = line number)
    """
    # initialize return value dictionaries
    valid_lines = {}
    invalid_lines = {}

    try:
        # loop over all input lines
        for line_num, order in inp_orders.items():
            inp_cash = order.cash_avail
            inp_price = order.price
            inp_wrappers = order.wrappers_needed
            candy_type = order.candy_type

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
                    valid_lines[line_num] = Order(int(inp_cash), int(inp_price), int(inp_wrappers), candy_type)
            else:
                if line_num not in invalid_lines:
                    new_line = '|'.join([inp_cash, inp_price, inp_wrappers, candy_type])
                    invalid_lines[line_num] = InputError(line_num, new_line, err_msgs)

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

    try:
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

    except EOFError as ex:
        return 1, write_cnt, ex

    except FileNotFoundError as ex:
        return 2, write_cnt, ex

    except RuntimeError as ex:
        return 3, write_cnt, ex
