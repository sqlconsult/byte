#!/usr/bin/env python3

import constants
import candy


def test_bonus_candy():
    """
    Test bonus candy allocation
    :return:
    """
    #
    # dark         --> 1 dark
    # milk         --> 1 milk + 1 sugar free
    # sugar free   --> 1 dark + 1 constants.SUGAR_FREE
    # white        --> 1 sugar free + 1 constants.WHITE
    #
    bonus = {
        constants.DARK: {constants.DARK: 1, constants.MILK: 0, constants.SUGAR_FREE: 0, constants.WHITE: 0},
        constants.MILK: {constants.DARK: 0, constants.MILK: 1, constants.SUGAR_FREE: 1, constants.WHITE: 0},
        constants.SUGAR_FREE: {constants.DARK: 1, constants.MILK: 0, constants.SUGAR_FREE: 1, constants.WHITE: 0},
        constants.WHITE: {constants.DARK: 0, constants.MILK: 0, constants.SUGAR_FREE: 1, constants.WHITE: 1},
        'unknown': {constants.DARK: 0, constants.MILK: 0, constants.SUGAR_FREE: 0, constants.WHITE: 0}
    }

    for key, value in bonus.items():
        dark, milk, sugar_free, white = candy.bonus_candy(key)
        assert dark == value[constants.DARK]
        assert milk == value[constants.MILK]
        assert sugar_free == value[constants.SUGAR_FREE]
        assert white == value[constants.WHITE]


def test_candy_calc():
    """
    Test promotional candy is correctly allocated for 4 test orders
    :return:
    """
    result = candy.candy_calc(14, 2, 6, constants.MILK)
    assert result[constants.DARK] == 0
    assert result[constants.MILK] == 8
    assert result[constants.SUGAR_FREE] == 1
    assert result[constants.WHITE] == 0

    result = candy.candy_calc(12, 2, 5, constants.MILK)
    assert result[constants.DARK] == 0
    assert result[constants.MILK] == 7
    assert result[constants.SUGAR_FREE] == 1
    assert result[constants.WHITE] == 0

    result = candy.candy_calc(12, 4, 4, constants.DARK)
    assert result[constants.DARK] == 3
    assert result[constants.MILK] == 0
    assert result[constants.SUGAR_FREE] == 0
    assert result[constants.WHITE] == 0

    result = candy.candy_calc(6, 2, 2, constants.SUGAR_FREE)
    assert result[constants.DARK] == 3
    assert result[constants.MILK] == 0
    assert result[constants.SUGAR_FREE] == 5
    assert result[constants.WHITE] == 0
