#!/usr/bin/env python3

import os

import candy
import model
import view


def display_invalid_orders(invalid_orders):
    """
    Display invalid input orders
    :param invalid_orders:  List of InvalidOrders with error messages to display
    :return:                True
    """
    for invalid_order in invalid_orders:
        err_msg = 'Line nuumber: {line_num}    Line: {line}'. \
            format(line_num=invalid_order.line_num, line=invalid_order.line)
        view.display_msg(err_msg)
        for e in invalid_order.errors:
            err_msg = '{err_str}'.format(err_str=e)
            view.display_msg(err_msg)
    return True


def files_exist(input_params):
    """
    Validate inut and output directories and files exist
    :param input_params: Dictionary containing input and output directory and file names
    :return:             False if an error is detected, else True
    """
    # does input directory exist?
    if not os.path.isdir(input_params['input_dir']):
        input_params['files_exist'] = False
        msg = 'ERROR: Input directory {0} does not exist'.format(input_params['input_dir'])
        view.display_msg(msg)

    # does input order file exist?
    input_params['input_file_path'] = os.path.join(input_params['input_dir'], input_params['input_file'])
    if not os.path.isfile(input_params['input_file_path']):
        input_params['files_exist'] = False
        msg = 'ERROR: Input orders file {0} does not exist'.format(input_params['input_file_path'])
        view.display_msg(msg)

    # if output directory does not exist, create it
    if not os.path.isdir(input_params['output_dir']):
        msg = 'WARNING: Output directory {0} does not exist and will be created'.format(input_params['output_dir'])
        view.display_msg(msg)
        os.mkdir(input_params['output_dir'])

    # if output file exists, overwrite it
    input_params['output_file_path'] = os.path.join(input_params['output_dir'], input_params['output_file'])
    if os.path.isfile(input_params['output_file_path']):
        msg = 'WARNING: Output file already exists and will be overwritten'.format(input_params['output_file_path'])
        view.display_msg(msg)

    return input_params


def main():
    """
    Main processing method
    :return:
    """
    # set & validate input parameters
    input_params = {'input_dir': '../input',
                    'input_file': 'orders.csv',
                    'output_dir': '../output',
                    'output_file': 'redemptions.csv',
                    'input_file_path': '',
                    'output_file_path': '',
                    'files_exist': True}

    validated_params = files_exist(input_params)

    if validated_params['files_exist']:
        # display app starting message to user
        app_name = __file__.split('.')[0]
        msg = '===== Starting {app_name}====='.format(app_name=app_name)
        view.display_msg(msg)

        # read input file to get valid and invalid orders
        valid_orders, invalid_orders, read_successful = read_order_file(input_params['input_file_path'])

        # process valid orders when successful in reading & validating input file
        if read_successful:
            # process valid orders
            valid_order_cnt = len(valid_orders)
            if valid_order_cnt > 0:
                msg = 'Processing {0} valid orders'.format(valid_order_cnt)
                view.display_msg(msg)

                orders_to_write = process_valid_orders(valid_orders)

                write_output_orders_file(orders_to_write, input_params['output_file_path'])

            # display invalid orders
            if len(invalid_orders) > 0:
                display_invalid_orders(invalid_orders)

    # display app completion message to user
    print('===== Done =====')


def process_valid_orders(valid_orders):
    """
    Takes a valid orders, processes and writes to output file
    :param valid_orders: List of valid input orders to process
    :return:             List of dictionaries to write.  1 dictionary for each order.  Each dictionary contains the
                         number of dark, milk, sugar free and white wrappers to write
    """
    # calculate 1) number of wrappers they ordered + 2) number of bonus wrappers they earned
    orders_to_write = []
    for o in valid_orders:
        total_wrappers = candy.candy_calc(o.cash_avail,
                                          o.price,
                                          o.wrappers_needed,
                                          o.candy_type)
        orders_to_write.append(total_wrappers)

    return orders_to_write


def read_order_file(input_file_name):
    """
    Reads input order file invalid (InvalidOrder) orders
    :param input_file_name: Path to orders input file
    :return:                1 - list of valid orders (ValidOrder)
                            2 - list of invalid orders (InvalidOrder)
                            3 - read_successful True if reading file is successful, else False
    """
    # read & validate orders file (valid_orders and/or invalid_orders may be length = 0)
    valid_orders = []
    invalid_orders = []
    read_successful = True
    try:
        valid_orders, invalid_orders = model.read_file(input_file_name)

    except FileNotFoundError as ex:
        msg = 'FileNotFoundError (check file path) occurred while reading {path}.  Exception=[{exception}'. \
            format(path=input_file_name, exception=ex)
        view.display_msg(msg)
        read_successful = False

    except StopIteration:
        msg = 'StopIteration (check file size) occurred while reading {path}.'. \
            format(path=input_file_name)
        view.display_msg(msg)
        read_successful = False

    except Exception as ex:
        msg = 'Unknown exception {ex} occurred while reading {path}.'. \
            format(ex=ex, path=input_file_name)
        view.display_msg(msg)
        read_successful = False

    finally:
        return valid_orders, invalid_orders, read_successful


def write_output_orders_file(orders_to_write, output_file_name):
    """
    Writes final orders file
    :param orders_to_write:   List of dictionaries to write.  1 dictionary for each order.  Each dictionary
                              contains the number of dark, milk, sugar free and white wrappers to write
    :param output_file_name:  Path to output file
    :return:                  Number of lines written or zero on error
    """
    written_order_cnt = 0
    try:
        written_order_cnt = model.write_orders(orders_to_write, output_file_name)
        msg = 'Successfully wrote {write_cnt} records to {output_file_name}'. \
            format(write_cnt=written_order_cnt,
                   output_file_name=output_file_name)
        view.display_msg(msg)
    except Exception as ex:
        msg = 'Unexpected error occurred while writing {path}.  Exception=[{exception}'. \
            format(path=output_file_name, exception=ex)
        view.display_msg(msg)
    finally:
        return written_order_cnt


if __name__ == '__main__':
    main()
