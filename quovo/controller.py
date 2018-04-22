#!/usr/bin/env python3

import logging
import model
import view

import logger


def debit_loop(db_name, module_logger):

    create_input = ['c', 'create']      # create account
    charge_input = ['r', 'charge']      # charge account
    hold_input = ['h', 'hold']          # place hold on account
    settle_input = ['s', 'settle']      # release hold & charge actual amount
    quit_input = ['q', 'quit']          # exit the game

    # valid input is combination of all other inputs
    valid_actions = create_input + charge_input + hold_input + settle_input + quit_input

    msg = 'Valid actions are: [' + ','.join(valid_actions) + ']'
    view.show_user_results(msg)

    # Loop until user requests to quit
    switched_on = True
    while switched_on:
        user_input = view.menu().lower()

        # perform user requested action
        if user_input in create_input:
            # create_account(initial_balance)
            amt, ignore1, ignore2, valid_input = get_user_input(['amount'])

            if valid_input:
                acct_num = model.create_account(amt, db_name)
                if acct_num == -1:
                    view.show_user_results('Failed to create account')
                else:
                    msg = 'New account number = {acct_num} Initial balance = {amt}.'.\
                        format(acct_num=acct_num, amt=amt)
                    view.show_user_results(msg)
                    module_logger.info(msg)

        elif user_input in charge_input:
            # charge(account_id, amount)
            # get user input
            amt, acct_num, ignore2, valid_input = get_user_input(['amount', 'account'])

            # if user entered valid input, process it
            if valid_input:
                ret_sts = model.charge(acct_num, amt, db_name)
                if ret_sts == 0:
                    msg = 'Successfully charge account {acct_num} {amt}'.\
                        format(acct_num=acct_num, amt=amt)
                elif ret_sts == -1:
                    msg = 'Failed to charge account {acct_num}'.format(acct_num=acct_num)
                elif ret_sts == -2:
                    msg = 'Insufficient funds to charge account {acct_num} {amt}'.\
                        format(acct_num=acct_num, amt=amt)
                else:
                    msg = 'Unknown status returned from model.charge {ret_sts}'.\
                        format(ret_sts=ret_sts)
                view.show_user_results(msg)
                module_logger.info(msg)

        elif user_input in hold_input:
            # hold(account_id, vendor_id, amount)
            # get user input
            amt, acct_num, vendor_id, valid_input = get_user_input(['amount', 'account', 'vendor'])

            # if user entered valid input, process it
            if valid_input:
                ret_sts = model.hold(acct_num, vendor_id, amt, db_name)
                if ret_sts == 0:
                    msg = 'Hold on account {acct_num} for {amt} is successful'.\
                        format(acct_num=acct_num, amt=amt)
                elif ret_sts == -1:
                    msg = 'Failed to place hold on account {acct_num} for {amt}'.\
                        format(acct_num=acct_num, amt=amt)
                elif ret_sts == -2:
                    msg = 'Insufficient funds to place hold on account {acct_num} for {amt}'.\
                        format(acct_num=acct_num, amt=amt)
                elif ret_sts == -3:
                    msg = 'Only 1 hold per vendor id for account {acct_num}'.\
                        format(acct_num=acct_num)
                else:
                    msg = 'Unknown status returned from model.hold {ret_sts}'.\
                        format(ret_sts=ret_sts)
                view.show_user_results(msg)
                module_logger.info(msg)

        elif user_input in settle_input:
            # settle_hold(account_id, vendor_id, actual_amount)
            # get user input
            amt, acct_num, vendor_id, valid_input = get_user_input(['amount', 'account', 'vendor'])

            if valid_input:
                ret_sts = model.settle_hold(acct_num, vendor_id, amt, db_name)
                if ret_sts == 0:
                    msg = 'Settle hold on account {acct_num} for {amt} is successful'.\
                            format(acct_num=acct_num, amt=amt)
                elif ret_sts == -1:
                    msg = 'Failed to settle hold on account {acct_num}'.\
                            format(acct_num=acct_num)
                elif ret_sts == -2:
                    msg = 'Insufficient funds to settle hold on account {acct_num} for {amt}'. \
                        format(acct_num=acct_num, amt=amt)
                else:
                    msg = 'Unknown status returned from model.hold {ret_sts}'. \
                        format(ret_sts=ret_sts)
                view.show_user_results(msg)
                module_logger.info(msg)

        elif user_input in quit_input:
            view.show_user_results('Thanks for playing.  Goodbye!')
            module_logger.info('User entered quit')
            switched_on = False
            # break
        else:
            view.show_user_results('Invalid input')
            msg = 'Valid actions are: [' + ','.join(valid_actions) + ']'
            view.show_user_results(msg)


def get_user_input(action):
    amt = None
    acct_num = None
    vendor_id = None

    valid_input = True
    if 'amount' in action:
        amt = view.get_user_input('Enter amount:', 5)
        if not is_number(amt, 'float'):
            view.show_user_results('Charge amount must be a valid number')
            valid_input = False
        else:
            if float(amt) < 0:
                view.show_user_results('Amount must be a positive number')
                valid_input = False

    if 'account' in action:
        acct_num = view.get_user_input('Enter account number:', 5)
        if not is_number(acct_num, 'int'):
            view.show_user_results('Account number must be a valid integer')
            valid_input = False
        else:
            if int(acct_num) < 0:
                view.show_user_results('Account number must be a positive integer')
                valid_input = False

    if 'vendor' in action:
        vendor_id = view.get_user_input('Enter vendor id:', 5)
        if not is_number(vendor_id, 'int'):
            view.show_user_results('Vendor id must be a valid integer')
            valid_input = False
        else:
            if int(vendor_id) < 0:
                view.show_user_results('Vendor id must be a positive integer')
                valid_input = False

    r_amt = float(amt) if valid_input and amt is not None else None
    r_acct = int(acct_num) if valid_input and acct_num is not None else None
    r_vendor = int(vendor_id) if valid_input and vendor_id is not None else None
    return r_amt, r_acct, r_vendor, valid_input


def is_number(s, typ):
    """
    :param s:   String to check
    :param typ: Numeric type ( 'float' | 'int' }
    :return:    Returns True is s is a number, else False
    """
    try:
        if typ == 'float':
            float(s)
        elif type == 'int':
            int(s)
        return True
    except ValueError:
        return False


def main():
    # Start logger
    app_name = __file__.split('.')[0]
    logger.start_logger(app_name)

    module_logger = logging.getLogger('{app_name}.controller'.format(app_name=app_name))
    module_logger.info('===== Starting =====')

    # db name
    db_name = 'debit.db'
    # db_name = ':memory:'

    # start the trading
    debit_loop(db_name, module_logger)

    module_logger.info('===== Done =====')


if __name__ == '__main__':
    main()
