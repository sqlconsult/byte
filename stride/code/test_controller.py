#!/usr/bin/env python3

import constants as constants
import controller as controller
import model as model
import order as order


def test_display_invalid_orders():
    #
    # test invalid data is displayed
    #
    invalid_orders = []
    invalid_test_order = order.InputOrder(1, 'a,b,c,"d"\n')
    invalid_orders.append(model.validate_input_order(invalid_test_order))

    invalid_test_order = order.InputOrder(2, 'e,f,g,"h"\n')
    invalid_orders.append(model.validate_input_order(invalid_test_order))

    ret_val = controller.display_invalid_orders(invalid_orders)

    assert ret_val


def test_process_valid_orders():
    #
    # test valid input orders are correctly added to orders to write
    #
    valid_orders = [order.ValidOrder(1, '12', '2', '5', 'milk'),
                    order.ValidOrder(2, '12', '4', '4', 'dark')]

    orders_to_write = controller.process_valid_orders(valid_orders)

    # there should be exactly 2 orders to write
    assert len(orders_to_write) == 2

    # the 1st order should be {'white': 0, 'milk': 7, 'sugar free': 1, 'dark': 0}
    assert orders_to_write[0][constants.WHITE] == 0
    assert orders_to_write[0][constants.MILK] == 7
    assert orders_to_write[0][constants.SUGAR_FREE] == 1
    assert orders_to_write[0][constants.DARK] == 0

    # the 2nd order should be {'white': 0, 'milk': 0, 'sugar free': 0, 'dark': 3}
    assert orders_to_write[1][constants.WHITE] == 0
    assert orders_to_write[1][constants.MILK] == 0
    assert orders_to_write[1][constants.SUGAR_FREE] == 0
    assert orders_to_write[1][constants.DARK] == 3
