#!/usr/bin/env python3

import constants


def bonus_candy(candy_type):
    """
    :param candy_type:  source candy type { 'milk', 'white', 'sugar free', 'dark' }
    :return:            number of milk, white, sugar free and dark bonus chocolates
    """
    # initialize return values
    milk = 0
    white = 0
    sugar_free = 0
    dark = 0

    # for milk we give 1 milk + 1 sugar free
    if candy_type == constants.MILK:
        milk = 1
        sugar_free = 1

    # for white we give 1 white + 1 sugar free
    elif candy_type == constants.WHITE:
        white = 1
        sugar_free = 1

    # for sugar free we give 1 sugar free + 1 dark
    elif candy_type == constants.SUGAR_FREE:
        sugar_free = 1
        dark = 1

    # for dark we give 1 dark
    elif candy_type == constants.DARK:
        dark = 1

    return dark, milk, sugar_free, white


def candy_calc(cash, price, wrappers_needed_for_exch, candy_type):
    """
    :param cash:        Cash amount to spend
    :param price:       Price for each chocolate
    :param wrappers_needed_for_exch:    # of wrappers needed for a bonus
    :param candy_type:  Chocolate type { 'milk', 'white', 'sugar free', 'dark' }
    :return:            Final number of milk, white, sugar free and dark chocolates
    """
    # used wrappers by candy type
    cnt_used = {
        constants.MILK: 0,
        constants.DARK: 0,
        constants.WHITE: 0,
        constants.SUGAR_FREE: 0
    }

    # bonus wrappers by candy type
    cnt_bonus = {
        constants.MILK: 0,
        constants.DARK: 0,
        constants.WHITE: 0,
        constants.SUGAR_FREE: 0
    }

    # get initial number of candies they can buy
    cnt_used[candy_type] = cash // price

    # initialize bonus candies found
    bonus_candy_found = True

    # loop until there are no more bonus candies available
    # a.k.a loop until no more candies can be earned
    while bonus_candy_found:
        # reset bonus candy found flag
        bonus_candy_found = False
        # iterate over wrappers, if we can exchange wrappers for more wrappers, then make the exchange
        for candy_type, num_wrappers in cnt_used.items():
            # check if we have enough wrappers to exchange for more candy
            if num_wrappers >= wrappers_needed_for_exch:

                # If we make the exchange, we need to check in future if we can make more exchanges
                # bonus_candy_found True will force loop to check again
                bonus_candy_found = True

                # subtract the wrappers we are exchanging
                cnt_used[candy_type] = num_wrappers - wrappers_needed_for_exch

                # add those wrappers to consumed wrappers
                cnt_bonus[candy_type] += wrappers_needed_for_exch

                # exchange wrappers for bonus wrappers (key = candy type)
                dark, milk, sugar_free, white = bonus_candy(candy_type)

                # add bonus wrappers to our total wrappers
                cnt_used[constants.DARK] += dark
                cnt_used[constants.MILK] += milk
                cnt_used[constants.SUGAR_FREE] += sugar_free
                cnt_used[constants.WHITE] += white

    # now that we are out of the loop, we have no more exchanges
    # so we use all remaining wrappers
    for k, v in cnt_used.items():
        cnt_bonus[k] += v

    # return dictionary of wrappers
    return cnt_bonus
