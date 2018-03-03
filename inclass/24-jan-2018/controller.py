#!/usr/bin/env python3.6
import model
import view

# This file's role in application: routing

def game_loop():
    buy_input = ['b', 'buy']
    sell_input = ['s', 'sell']
    quit_input = ['q','quit']

    valid_input = buy_input + sell_input + quit_input

    switched_on = True
    while switched_on:
        user_input = view.menu().lower()
        if user_input in valid_input:
            if user_input in buy_input:
                #print('Progress to business logic for buy')
                x = model.buy()
                return x
            elif user_input in sell_input:
                print('Progress to business logic for sell')
            elif user_input in quit_input:
                print('Thanks for playing.  Goodbye!')
                break
                #switched_on = False
            print('Progress to next step')
        else:
            print('Invalid input')
            game_loop()
            # switched_on = False


if __name__ == '__main__':
    game_loop()
