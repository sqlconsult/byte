from bs4 import BeautifulSoup
import requests
from random import randint

class Roulette:
    winning_spaces = ''
    payout = ''
    odds_against_fr = ''
    expected_val_fr = ''
    odds_against_us = ''
    expected_val_us = ''

    def __init__(self, win_spc, pay, odds_fr, expected_fr, odds_us, expected_us):
        self.winning_spaces = win_spc
        self.payout = pay
        self.odds_against_fr = odds_fr
        self.expected_val_fr = expected_fr
        self.odds_against_us = odds_us
        expected_val_us = expected_us

def make_odds(win_spc, pay, odds_fr, expected_fr, odds_us, expected_us):
    retVal = Roulette(win_spc, pay, odds_fr, expected_fr, odds_us, expected_us)
    return retVal

def roulette():
    # open downloaded html file that has roulette odds in it
    response = requests.get('http://en.wikipedia.org/wiki/Roulette#Bet_odds_table').text
    soup = BeautifulSoup(response, 'html.parser')

    # there are 3 tables on this page with class name = 'wikitable'
    wikiTables = soup.find_all('table', class_='wikitable')

    # the odds table is the 2nd table in the list
    odds_table = wikiTables[1]

    # get table headers into a list object
    headers = odds_table.find_all('th')

    # parse headers & retrieve text into an array
    header_text = []
    for header in headers:
        tmpStr = header.text
        tmp = tmpStr.replace('\n', ' ')
        header_text.append(tmp)

    # get individual bet odds & payout from td entries
    odds = odds_table.find_all('td')

    numBets = int(len(odds) / 7)

    # print('numBets: ', numBets, 'len(odds): ', len(odds))

    # print('odds html:')
    # i = 0
    # for o1 in odds:
    #     print(i, o1)
    #     i += 1

    betting_tbl = {}
    idx = 0
    for bet in range(numBets):
        bet_name = odds[idx].text
        idx += 1
        win_spc = odds[idx].text
        idx += 1
        pay = odds[idx].txt
        idx += 1
        odds_fr = odds[idx].txt
        idx += 1
        expected_val_fr = odds[idx].text
        idx += 1
        odds_us = odds[idx].text
        idx += 1
        expected_val_us = odds[idx].text
        idx += 1

        o = make_odds(win_spc, pay, odds_fr, expected_val_fr, odds_us, expected_val_us)
        key = bet_name.lower()
        betting_tbl[key] = o

    # for key, value in betting_tbl.items():
    #    print('Bet name: ', key, 'Odds: ', betting_tbl[key].odds_against_us)
    return betting_tbl


def SpinWheel(bet_name, num1, num2):
    flag = 'lost'     # or 'won'

    # 0 - 36 numbers on wheel + 00 = 37
    win_num = randint(0 , 37)
    # testing --- win_num = 8

    # check winning number against their bet
    if bet_name == 'straight_up':
        if win_num == num1: flag = 'won'

    elif bet_name == '00':
        if win_num == 37: flag = 'won'

    elif bet_name == '1 to 18':
        if win_num >= 1 and win_num <= 18: flag = 'won'

    elif bet_name == 'top line or basket':
        if win_num == 37 or win_num <= 3: flag = 'won'

    elif bet_name == 'split':
        if win_num == num1 or win_num == num2: flag = 'won'

    elif bet_name == '1st dozen':
        if win_num >= 1 and win_num <= 12: flag = 'won'

    elif bet_name == '2nd dozen':
        if win_num >= 13 and win_num <= 24: flag = 'won'

    elif bet_name == 'row':
        if win_num == 0 or win_num ==37: flag = 'won'

    elif bet_name == '1st column':
        numbers = list(range(1,37,3))
        if win_num in numbers: flag = 'won'

    elif bet_name == 'even':
        if win_num % 2 == 0: flag = 'won'

    elif bet_name == '3rd column':
        numbers = list(range(3,39,3))
        if win_num in numbers: flag = 'won'

    elif bet_name == '3rd dozen':
        if win_num >= 25 and win_num <= 36: flag = 'won'

    elif bet_name == 'odd':
        if win_num % 2 == 1: flag = 'won'

    elif bet_name == 'street':
        if win_num >= num1 and win_num <= num1 + 2: flag = 'won'

    elif bet_name == 'corner':
        numbers = [ num1, num1+1, num1+3, num1+4]
        if win_num in numbers: flag = 'won'

    elif bet_name == 'red':
        numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        if win_num in numbers: flag = 'won'

    elif bet_name == '19 to 36':
       if win_num >= 19 or win_num <= 36: flag = 'won'

    elif bet_name == '2nd column':
        numbers = list(range(2,38,3))
        if win_num in numbers: flag = 'won'

    elif bet_name == 'black':
        numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        if win_num in numbers: flag = 'won'

    elif bet_name == 'six line':
        if win_num >= num1 and win_num <= num1 + 5: flag = 'won'

    return flag


if __name__ == '__main__':
    bet_tbl = {}
    bet_tbl = roulette()

    # for key, value in bet_tbl.items():
    #     print('Bet name: ', key, 'Odds: ', bet_tbl[key].odds_against_us)

    exit_loop = False

    while not exit_loop:
        print("Enter your bet name or 'quit' to quit: ")
        bet_name_inp = input()
        bet_name = bet_name_inp.lower()

        if bet_name ==  'quit':
            exit_loop = True
        else:
            if bet_name in bet_tbl:
                # print('Your odds for bet name: ' + bet_name_inp, ' are ' + bet_tbl[bet_name].odds_against_us)
                inp1 = ''
                inp2 = ''
                num1 = -1
                num2 = -1
                if bet_name == 'split':
                    inp1, inp2 = map(int,input('Please input your two numbers (with a comma in between): ').strip().split(","))
                    num1 = int(inp1)
                    num2 = int(inp2)
                elif bet_name == 'street' or bet_name == 'corner' or bet_name == 'six line' or bet_name == 'straight up':
                    inp1 = input('Please input first number in bet list: ')
                    num1 = int(inp1)
                win_lost = SpinWheel(bet_name, num1, num2)
                print('You ' + win_lost + '!')
            else:
                print('Invalid bet name [' + bet_name_inp + '].  Valid bet names are:')
                v = ', '.join(['%s' % (key) for (key, value) in bet_tbl.items()])
                print(v)
    print('Done.')

