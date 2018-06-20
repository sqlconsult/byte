#!/usr/bin/env python3

import os

import candy
import model
import view


def main():
    # source input file path
    input_file_name = os.path.join('input', 'orders.csv')

    # target output file path
    output_file_name = os.path.join('output', 'redemptions.csv')

    # display app starting message to user
    app_name = __file__.split('.')[0]
    msg = '===== Starting {app_name}====='.format(app_name=app_name)
    view.display_msg(msg)

    # read orders file into list of class Order
    read_error_code, inp_orders, read_exception = model.read_file(input_file_name)

    if read_error_code > 0:
        process_read_write_error(read_error_code, 'read', read_exception, input_file_name)
    else:
        input_order_cnt = len(inp_orders)
        valid_orders, invalid_orders, validate_status, ex = model.validate_input_data(inp_orders)

        valid_cnt = len(valid_orders)
        invalid_cnt = len(invalid_orders)

        if validate_status < 0:
            msg = 'RuntimeError occurred while validating input orders. {0} of {1} orders are invalid'.\
                format(invalid_cnt, input_order_cnt)
            view.display_msg(msg)

        if valid_cnt > 0:
            msg = '{0} of {1} orders are valid'.format(valid_cnt, input_order_cnt)
            view.display_msg(msg)

            # calculate 1) number of wrappers they ordered + 2) number of bonus wrappers they earned
            redemptions_to_write = []
            for line_no, order in valid_orders.items():
                total_wrappers = candy.candy_math(order.cash_avail,
                                                  order.price,
                                                  order.wrappers_needed,
                                                  order.candy_type)

                redemptions_to_write.append(total_wrappers)

            # write redemptions output file
            write_error_code, write_cnt, write_exception = \
                model.write_redemptions(redemptions_to_write, output_file_name)

            if write_error_code > 0:
                process_read_write_error(write_error_code, 'write', write_exception, output_file_name)
            else:
                msg = 'Successfully wrote {write_cnt} records to {output_file_name}'.\
                    format(write_cnt=write_cnt,
                           output_file_name=output_file_name)
                view.display_msg(msg)

    # display app completion message to user
    print('===== Done =====')


def process_read_write_error(error_code, action, exception, path):
    """
    :param error_code: 1 = EOFError, 2 = FileNotFoundError, 3 = RuntimeError
    :param action:     'read' or 'write'
    :param exception:  System generated exception
    :param path:       Path to file being read or written
    :return:           True
    """
    # Map error code to string
    error_types = ['', 'EOFError', 'FileNotFoundError', 'RuntimeError', 'StopIteration']

    # Build error message
    msg = '{error_type} occurred while {action}ing {path}.  Exception=[{exception}'.\
        format(error_type=error_types[error_code],
               action=action,
               path=path,
               exception=exception)
    # Display error message
    view.display_msg(msg)


if __name__ == '__main__':
    main()
