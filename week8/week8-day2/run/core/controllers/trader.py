#!/usr/bin/env python3
import time
from flask import Blueprint, render_template, request
from core.controllers import model

controller = Blueprint('traders', __name__, url_prefix='')


db_name = 'run/core/controllers/stock.db'     # db name


@controller.route('/', methods=['GET'])
def home_page():
    if request.method == 'GET':
        # This is an HTTP get request.
        return render_template('Login.html')


@controller.route('/Login', methods=['POST'])
def login_page():
    # print('db_name:', db_name)
    if request.method == 'POST':
        # This is an HTTP post request.
        user_inp = request.form['user_id']
        login_id = int(user_inp)
        cash_left, super_user, created_on = model.IsValidUserId(db_name, login_id)

        if cash_left == -1:
            return render_template('Register.html')
        else:
            return render_template('Router.html', login_id=user_inp)


@controller.route('/Register', methods=['POST'])
def register_page():
    if request.method == 'POST':
        user_inp = request.form['cash_amt']

        if len(user_inp) == 0:
            return render_template('Login.html')

        # make sure user input valid number
        try:
            cash_amt = float(user_inp)
        except ValueError:
            return render_template('Login.html')

        super_user = 'False'     # TODO how to set super user flag???
        created_on = int(time.time())
        login_id = model.AddNewUser(db_name, cash_amt, cash_amt, super_user, created_on)
        return render_template('Router.html', login_id=login_id)


@controller.route('/action_router/', methods=['GET', 'POST'])
def router_page():
    if request.method == 'POST':
        user_action = request.form['action']
        login_id = request.form['login_id']
        if user_action == 'buy_stock':
            return render_template('Trade.html', buy_sell='Buy', login_id=login_id)
        elif user_action == 'sell_stock':
            return render_template('Trade.html', buy_sell='Sell', login_id=login_id)
        elif user_action == 'cash':
            return render_template('Cash.html', login_id=login_id)
        elif user_action == 'ticker_info':
            return render_template('TickerInfo.html', login_id=login_id)
        elif user_action == 'positions':
            positions_dict = get_positions(login_id)
            return render_template('Positions.html',
                                   login_id=login_id,
                                   data=positions_dict)
        else:
            pass
    elif request.method == 'GET':
        print('router get')


@controller.route('/TickerInfo', methods=['GET', 'POST'])
def ticker_info_page():
    if request.method == 'POST':
        login_id = request.form['login_id']
        ticker = request.form['ticker']
        company = request.form['company']

        stock_to_lookup = ''
        if len(ticker) > 0:
            stock_to_lookup = ticker
        elif len(company) > 0:
            stock_to_lookup = company

        if len(stock_to_lookup) > 0:
            print(stock_to_lookup)
            lk_ticker, lk_name, lk_exchange, lk_last_price = model.GetLastPrice(stock_to_lookup)
            last_prc = str(lk_last_price)
            return render_template('TickerDisplay.html',
                                   ticker=lk_ticker,
                                   company=lk_name,
                                   exchange=lk_exchange,
                                   last_price=last_prc,
                                   login_id=login_id)
        else:
            msg = 'Invalid ticker or company name'
            print(msg)
            return render_template('DisplayResults.html',
                                   header_to_show='Stock Lookup Results',
                                   msg_to_show=msg,
                                   login_id=str(login_id))


@controller.route('/TickerDisplay', methods=['GET', 'POST'])
def ticker_display_page():
    if request.method == 'POST':
        login_id = request.form['login_id']
        return render_template('Router.html', login_id=login_id)


@controller.route('/Trade', methods=['GET', 'POST'])
def trade_page():
    if request.method == 'POST':
        # get user inputs
        inp_shares = request.form['shares']
        inp_stock_to_trade = request.form['stock_to_trade']
        login_id = request.form['login_id']
        int_login_id = int(login_id)

        if len(inp_shares) == 0 or len(inp_stock_to_trade) == 0:
            msg = 'Either invalid ticker or number of shares to trade'
            return render_template('DisplayResults.html',
                                   header_to_show='Trade Results',
                                   msg_to_show=msg,
                                   login_id=login_id)

        ticker, name, exchange, last_price = model.GetLastPrice(inp_stock_to_trade)

        num_shares = int(inp_shares)
        # print(input_shares, stock_to_lookup, login_id, ticker)

        trade_direction = request.form['trade_direction']
        trd_dir = trade_direction.lower()

        msg = ''
        if trd_dir == 'buy':
            ret_sts = model.BuyStock(db_name, int_login_id, ticker, num_shares)
            if ret_sts == -1:
                msg = 'Insufficient cash to execute transaction'
            else:
                msg = 'Buy successful'

        elif trd_dir == 'sell':
            ret_sts = model.SellStock(db_name, int_login_id, ticker, num_shares)

            if ret_sts == -1:
                msg = 'Must own stock before selling'
            elif ret_sts == -2:
                msg = 'Insufficient shares owned to execute transaction'
            elif ret_sts == 0:
                msg = 'Sell successful'
            else:
                msg = 'Unknown status returned from SellStock: {0}'.format(ret_sts)

        return render_template('DisplayResults.html',
                               header_to_show='Trade Results',
                               msg_to_show=msg,
                               login_id=login_id)


@controller.route('/DisplayResults', methods=['GET', 'POST'])
def trade_results_page():
    if request.method == 'POST':
        login_id = request.form['login_id']
        return render_template('Router.html', login_id=login_id)


@controller.route('/Cash', methods=['GET', 'POST'])
def cash_page():
    if request.method == 'POST':
        login_id = request.form['login_id']
        inp_cash_amount = request.form['cash_amount']

        if len(inp_cash_amount) == 0:
            msg = "Invalid cash amount"
            return render_template('DisplayResults.html',
                                   header_to_show='Cash Results',
                                   msg_to_show=msg,
                                   login_id=str(login_id))

        cash_amt = int(inp_cash_amount)

        add_or_remove = 'A' if cash_amt > 0 else 'R'

        if cash_amt != 0:
            ret_sts = model.AddOrRemoveCash(db_name, login_id, add_or_remove, cash_amt)
            total_cash = ret_sts[1]
            status_code = ret_sts[0]

            if status_code < 0:
                msg = 'Unable to remove more cash than in account.  '
                msg += 'Cash left in account: ${0:<12.2f}'.format(total_cash)

                return render_template('DisplayResults.html',
                                       header_to_show='Cash Results',
                                       msg_to_show=msg,
                                       login_id=login_id)

        # cash amount = 0, return to routing page
        return render_template('Router.html', login_id=login_id)


@controller.route('/Positions', methods=['GET', 'POST'])
def positions_page():
    if request.method == 'POST':
        login_id = request.form['login_id']
        return render_template('Router.html', login_id=login_id)


def get_positions(login_id):
    positions_tup = model.GetPositions(db_name, login_id, 'N')
    # print('Number of positions:', len(positions_tup))

    key = 1
    positions_dict = {}
    for tup in positions_tup:
        # get correctly typed values from tuple and save into dictionary
        user_id = int(tup[0])
        init_cash = float(tup[1])
        cash_left = float(tup[2])
        ticker = '' if tup[3] is None else tup[3]
        cash_bal = 0.0 if tup[4] is None else float(tup[4])
        shares = 0 if tup[5] is None else int(tup[5])

        # store position values in list
        c1 = '${:,.2f}'.format(init_cash)
        c2 = '${:,.2f}'.format(cash_left)
        c3 = '${:,.2f}'.format(cash_bal)
        values = [user_id, c1, c2, ticker, c3, shares]

        # add list to dictionary
        positions_dict[key] = values
        key += 1

    return positions_dict

