#!/usr/bin/env python3


def bonus_candy(candy_type):
    """
    :param candy_type:  source candy type
    :return:            number of milk, white, sugar free and dark bonus chocolates
    """
    # initialize return values
    milk = 0
    white = 0
    sugar_free = 0
    dark = 0

    # for milk we give 1 milk + 1 sugar free
    if candy_type == 'milk':
        milk = 1
        sugar_free = 1

    # for white we give 1 white + 1 sugar free
    if candy_type == 'white':
        white = 1
        sugar_free = 1

    # for sugar free we give 1 sugar free + 1 dark
    if candy_type == 'sugar free':
        sugar_free = 1
        dark = 1

    # for dark we give 1 dark
    if candy_type == 'dark':
        dark = 1

    return dark, milk, sugar_free, white


def candy_math(cash, price, wrappers_needed_for_exch, candy_type):
    """
    :param cash:        Cash amount to spend
    :param price:       Price for each chocolate
    :param wrappers_needed_for_exch:    # of wrappers needed for a bonus
    :param candy_type:  Chocolate type { 'milk', 'white', 'sugar free', 'dark' }
    :return:            Final number of milk, white, sugar free and dark chocolates
    """
    # used wrappers by candy type
    cnt_used = {
        'milk': 0,
        'dark': 0,
        'white': 0,
        'sugar free': 0
    }

    # bonus wrappers by candy type
    cnt_bonus = {
        'milk': 0,
        'dark': 0,
        'white': 0,
        'sugar free': 0
    }

    # get initial number of candies they can buy
    cnt_used[candy_type] = cash // price

    # initialize bonus candies found
    flag = True

    # loop until there are no more bonus candies available
    # a.k.a loop until no more candies can be earned
    while flag:
        # reset bonus candy found flag
        flag = False
        # iterate over wrappers, if we can exchange wrappers for more wrappers, then make the exchange
        for key, val in cnt_used.items():
            # check if we have enough wrappers to exchange for more candy
            if val >= wrappers_needed_for_exch:

                # If we make the exchange, we need to check in future if we can make more exchanges
                # flag True will force loop to check again
                flag = True

                # subtract the wrappers we are exchanging
                cnt_used[key] = val - wrappers_needed_for_exch

                # add those wrappers to consumed wrappers
                cnt_bonus[key] += wrappers_needed_for_exch

                # exchange wrappers for bonus wrappers (key = candy type)
                dark, milk, sugar_free, white = bonus_candy(key)

                # add bonus wrappers to our total wrappers
                cnt_used['dark'] += dark
                cnt_used['milk'] += milk
                cnt_used['sugar free'] += sugar_free
                cnt_used['white'] += white

    # now that we are out of the loop, we have no more exchanges
    # so we use all remaining wrappers
    for k, v in cnt_used.items():
        cnt_bonus[k] += v

    # return dictionary of wrappers
    return cnt_bonus


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


def main():
    """
    :return: Nothing, writes order to output file
    """
    # Start here
    app_name = __file__.split('.')[0]
    print('===== Starting {app_name}====='.format(app_name=app_name))

    # read input file
    with open('input/orders.csv') as f:
        with open('output/redemptions.csv', 'w+') as g:
            # skip header
            next(f)

            # process 1 line at time
            for line in f:
                # parse input line
                e = line.split(',')
                inp_cash = e[0]
                inp_price = e[1]
                inp_wrappers = e[2]
                candy_type = e[3].lower().replace('"', '')
                candy_type = candy_type[:-1]

                # validate input
                valid = validate_input_data(inp_cash, inp_price, inp_wrappers, candy_type)

                # proceed only with valid input
                if valid:
                    # convert input strings to int
                    cash, price, wrappers = int(inp_cash), int(inp_price), int(inp_wrappers)

                    # do the math
                    num_candy = candy_math(cash, price, wrappers, candy_type)

                    # display results
                    out_line = 'milk {milk},dark {dark},white {white},sugar free {sugar_free}\n'.\
                        format(milk=num_candy['milk'],
                               dark=num_candy['dark'],
                               white=num_candy['white'],
                               sugar_free=num_candy['sugar free'])
                    # print(out_line)
                    g.write(out_line)

    print('===== Done =====')


def tester():
    # test data validation
    print('Start automated tests')
    valid = validate_input_data('a', 'b', 'c', 'd')
    assert valid == False, 'Test #1 Failed'

    valid = validate_input_data('1.1', '2.2', '3.3', '4.4')
    assert valid == False, 'Test #2 Failed'

    valid = validate_input_data(10, 2, 3, '')
    assert valid == False, 'Test #3 Failed'

    valid = validate_input_data(10, 2, 3, 'xyz')
    assert valid == False, 'Test #4 Failed'

    valid = validate_input_data(10, 2, 3, 'milk')
    assert valid == True, 'Test #5 Failed'

    result = candy_math(14, 2, 6, 'milk')
    # {'milk': 7, 'sugar free': 2, 'white': 0, 'dark': 0}
    expected_results = result['dark'] == 0 and \
                       result['milk'] == 8 and \
                       result['sugar free'] == 1 and \
                       result['white'] == 0
    assert expected_results == True, 'Test #6 Failed'

    result = candy_math(14, 2, 6, 'milk')


    print('Automated tests completed')


def validate_input_data(inp_cash, inp_price, inp_wrappers, candy_type):
    valid = True
    if not is_number(inp_cash, 'int'):
        valid = False
        print('Invalid cash amount [{cash}]'.format(cash=inp_cash))

    if not is_number(inp_price, 'int'):
        valid = False
        print('Invalid price [{price}]'.format(price=inp_price))

    if not is_number(inp_wrappers, 'int'):
        valid = False
        print('Invalid wrappers [{wrappers}]'.format(wrappers=inp_wrappers))

    if candy_type not in ['milk', 'white', 'sugar free', 'dark']:
        valid = False
        print('Invalid candy type [{candy_type}]'.format(candy_type=candy_type))

    return valid


if __name__ == '__main__':
    # tester()
    main()
