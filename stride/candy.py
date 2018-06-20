#!/usr/bin/env python3

DARK = 'dark'
MILK = 'milk'
SUGAR_FREE = 'sugar free'
WHITE = 'white'


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
    if candy_type == MILK:
        milk = 1
        sugar_free = 1

    # for white we give 1 white + 1 sugar free
    elif candy_type == WHITE:
        white = 1
        sugar_free = 1

    # for sugar free we give 1 sugar free + 1 dark
    elif candy_type == SUGAR_FREE:
        sugar_free = 1
        dark = 1

    # for dark we give 1 dark
    elif candy_type == DARK:
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
        MILK: 0,
        DARK: 0,
        WHITE: 0,
        SUGAR_FREE: 0
    }

    # bonus wrappers by candy type
    cnt_bonus = {
        MILK: 0,
        DARK: 0,
        WHITE: 0,
        SUGAR_FREE: 0
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
        for candy_type, num_wrappers in cnt_used.items():
            # check if we have enough wrappers to exchange for more candy
            if num_wrappers >= wrappers_needed_for_exch:

                # If we make the exchange, we need to check in future if we can make more exchanges
                # flag True will force loop to check again
                flag = True

                # subtract the wrappers we are exchanging
                cnt_used[candy_type] = num_wrappers - wrappers_needed_for_exch

                # add those wrappers to consumed wrappers
                cnt_bonus[candy_type] += wrappers_needed_for_exch

                # exchange wrappers for bonus wrappers (key = candy type)
                dark, milk, sugar_free, white = bonus_candy(candy_type)

                # add bonus wrappers to our total wrappers
                cnt_used[DARK] += dark
                cnt_used[MILK] += milk
                cnt_used[SUGAR_FREE] += sugar_free
                cnt_used[WHITE] += white

    # now that we are out of the loop, we have no more exchanges
    # so we use all remaining wrappers
    for k, v in cnt_used.items():
        cnt_bonus[k] += v

    # return dictionary of wrappers
    return cnt_bonus
