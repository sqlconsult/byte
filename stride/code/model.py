#!/usr/bin/env python3

from order import InputOrder, ValidOrder, InvalidOrder
import constants


def is_number(s, typ):
    """
    For a given string (s) return true if valid float or int
    :param s:   String to check
    :param typ: Numeric type ( 'float' | 'int' }
    :return:    Returns True is s is a number, else False
    """
    ret_val = True
    try:
        if typ == 'float':
            float(s)
        elif typ == 'int':
            int(s)
        else:
            ret_val = False
        return ret_val
    except ValueError:
        ret_val = False
    finally:
        return ret_val


def read_file(file_path):
    """
    :param file_path: Path to order file to read
    :return:   1 - List of ValidOrders (can be length = 0)
               2 - List of InvalidOrders (can be length = 0)
    """
    # initialize return lists
    valid_orders = []
    invalid_orders = []

    # read input file
    with open(file_path) as f:
        # skip header
        next(f)

        # process file 1 line at time
        for line_num, line in enumerate(f):
            # parse input line
            imported_order = InputOrder(line_num, line)

            # validate input data
            order = validate_input_order(imported_order)

            # include returned object in correct list
            # order will be either class Order or InvalidOrder
            if type(order).__name__ == 'ValidOrder':
                valid_orders.append(order)
            else:
                invalid_orders.append(order)

    return valid_orders, invalid_orders


def validate_input_order(imported_order):
    """
    Validates input order and returns either a ValidOrder or InvalidOrder
    :param imported_order: Single imported line (Order)
    :return:               1 - Either
                                   a) a single valid   order (ValidOrder) or
                                   b) a single invalid order (InvalidOrder)
    """
    # validate input line and append each detected error to a list of error messages
    err_msgs = []

    valid = True
    if not is_number(imported_order.cash_avail, 'int'):
        msg = 'Invalid cash amount [{cash}]'.format(cash=imported_order.cash_avail)
        err_msgs.append(msg)
        valid = False

    if not is_number(imported_order.price, 'int'):
        msg = 'Invalid price [{price}]'.format(price=imported_order.price)
        err_msgs.append(msg)
        valid = False

    if not is_number(imported_order.wrappers_needed, 'int'):
        msg = 'Invalid wrappers [{wrappers}]'.format(wrappers=imported_order.wrappers_needed)
        err_msgs.append(msg)
        valid = False

    if imported_order.candy_type not in [constants.MILK, constants.WHITE, constants.SUGAR_FREE, constants.DARK]:
        msg = 'Invalid candy type [{candy_type}]'.format(candy_type=imported_order.candy_type)
        err_msgs.append(msg)
        valid = False

    if valid:
        valid_order = ValidOrder(imported_order.line_num,
                                 int(imported_order.cash_avail),
                                 int(imported_order.price),
                                 int(imported_order.wrappers_needed),
                                 imported_order.candy_type)
        return valid_order

    else:
        invalid_order = InvalidOrder(imported_order.line_num, imported_order.line, err_msgs)
        return invalid_order


def write_orders(orders_to_write, file_path):
    """
    :param orders_to_write: list of wrappers to write
    :param file_path:       path to output file
    """
    # initialize number of record written
    write_cnt = 0

    # output line template format
    line_to_write_fmt = 'milk {milk},dark {dark},white {white},sugar free {sugar_free}'

    # open output file
    with open(file_path, 'w+') as g:
        # loop over each set of wrappers and write to output file
        for o in orders_to_write:
            output_line = line_to_write_fmt.format(milk=o[constants.MILK],
                                                   dark=o[constants.DARK],
                                                   white=o[constants.WHITE],
                                                   sugar_free=o[constants.SUGAR_FREE])
            g.write(output_line + '\n')
            # increment records written counter
            write_cnt += 1

    # return error code = 0, success status, no exception
    return write_cnt

