#!/usr/bin/env python3

import os
import sys
import sqlite3
import time

import requests
import json

#
# IsValidUserId(fname, id)
#   given id return users.cash_left, users.super_user and users.created_on from users

# AddNewUser(fname, cash_left, super_user, created_on)
#    add new users entry and returns new users.id

# GetLastUerId(con, cur)
#    returns max(id) from users

# OpenConnection(fname)
#    returns con, cur for fname

# CloseConnection(con, cur)
#    closes con, cur

# PrintErr(info)
#    prints error from sys.exc_info()

# GetTicker(company_name)
#    given ticker or company name return ticker, name, exchange

# GetLastPrice(ticker_or_company)
#    given ticker or company name return ticker, name, exchange, last_price
#    call GetTicker to get ticker

# InsertTransaction(cur, id, ticker, buy_or_sell, num_shares, last_price)
#    insert buy or sell transaction in transactions table

# GetPosition(cur, id, ticker)
#    given id & ticker return position_id, agg_bal, shares from positions

# UpdatePosition(cur, id, ticker, buy_or_sell, num_shares, last_price)
#    for buy or sell, update positions table

# SellStock(fname, id, stock, num_shares)
#    calls InsertTransaction and UpdatePosition to sell a stock

# BuyStock(fname, id, stock, num_shares)
#    calls InsertTransaction, UpdatePosition and SetCurrentCash to buy a stock

# GetCurrentCash(cur, id)
#    for a given id get users.cash_left

# SetCurrentCash(cur, id, amt)
#    for a given id set users.cash_left = amt

# AddOrRemoveCash(fname, id, add_or_remove_flag, amt)
#    for a given id and flag add or remove users.cash_left by calling GetCurrentCash and SetCurrentCash

# current time in unix time (seconds after some date)
# cur_time = str(int(time.time()))


def IsValidUserId(fname, id):
    #
    # if id exists:
    #    return users.cash_left, users.super_user and users.created_on
    #    from database if id exists
    # else:
    #    return cash_left = -1, super_user = 'False', created_on = current datetime
    #
    cash_left = -1
    super_user = 'False'
    created_on = int(time.time())

    # print("fname:", fname)
    # print("script: sys.argv[0] is", repr(sys.argv[0]))
    # print("script: __file__ is", repr(__file__))
    # print("script: cwd is", repr(os.getcwd()))

    con, cur = OpenConnection(fname)

    sql = "SELECT cash_left, super_user, created_on " \
        + "FROM users WHERE id = " + str(id) + ";"

    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) > 0:
        cash_left = rows[0][0]
        super_user = rows[0][1]
        created_on = rows[0][2]

    CloseConnection(con, cur)

    return cash_left, super_user, created_on


def AddNewUser(fname, initial_cash, cash_left, super_user, created_on):
    # Add a new user to users database table and return the id
    con, cur = OpenConnection(fname)

    # build sql to insert this user
    sql = []
    sql.append("INSERT INTO users ( initial_cash, cash_left, super_user, created_on ) VALUES (")
    sql.append(str(initial_cash))
    sql.append(", ")
    sql.append(str(cash_left))
    sql.append(", '")
    sql.append(super_user)
    sql.append("', ")
    sql.append(str(created_on))
    sql.append(" );")

    sql_cmd = ''.join(str(x) for x in sql)

    # insert into database and commit
    cur.execute(sql_cmd)
    con.commit()

    id = GetLastUserId(cur)

    CloseConnection(con, cur)

    return id


def GetLastUserId(cur):
    # gets maximum (last) user.id from database
    # using open connection and cursor
    cur.execute("""SELECT MAX(id) from users;""")
    rows = cur.fetchall()
    id = rows[0][0]
    return id


def OpenConnection(fname):
    try:
        connection = sqlite3.connect(fname, check_same_thread=False)
        cursor     = connection.cursor()
        return connection, cursor
    except:
        PrintErr(sys.exc_info())
        return 1, 1



def CloseConnection(con, cur):
    try:
        cur.close()
        con.close()
        return 0
    except:
        PrintErr(sys.exc_info())


def PrintErr(info):
        print('Unexpected error')
        print('        type:', info[0])
        print('       value:', info[1])
        print('   traceback:', info[2])


def GetTicker(company_name):
    # Given a company name try to get the ticker, name and exchange
    #print('Enter GetTicker')
    # initialize return values to not found
    ticker = ''
    name = ''
    exchange = ''

    try:
        end_pt = 'http://dev.markitondemand.com/MODapis/Api/v2/Lookup/json?input={}'.format(company_name)
        response = requests.get(end_pt).text
        loads = json.loads(response)
        if len(loads) > 0:
            ticker   = loads[0]['Symbol']
            name     = loads[0]['Name']
            exchange = loads[0]['Exchange']
    except:
        PrintErr(sys.exc_info())

    #print('Exit GetTicker')
    return ticker, name, exchange


def GetLastPrice(ticker_or_company):
    # Given a ticker try and get the last price
    #print('Enter GetLastPrice')
    ticker, name, exchange = GetTicker(ticker_or_company)

    try:
        last_price = -1
        if ticker != '':
            quote_endpoint = 'http://dev.markitondemand.com/MODapis/Api/v2/Quote/json?symbol={}'.format(ticker)
            response = requests.get(quote_endpoint).text
            full_json = json.loads(response)
            if 'LastPrice' in full_json.keys():
                last_price = full_json['LastPrice']
    except:
        PrintErr(sys.exc_info())

    #print('Exit GetLastPrice')
    return ticker, name, exchange, last_price


def InsertTransaction(cur, id, ticker, xcn_type, num_shares, last_price):
    #print('Enter InsertTransaction')
    ts = int(time.time())
    sql = []
    sql.append("INSERT INTO trans ( user_id, ticker, buy_flag, shares, share_price, ts ) VALUES ( ")
    sql.append(str(id))
    sql.append(", '")
    sql.append(ticker)
    sql.append("', '")
    sql.append(xcn_type)
    sql.append("', ")
    sql.append(str(num_shares))
    sql.append(", ")
    sql.append("{0:.2f}".format(last_price))
    sql.append(", ")
    sql.append(str(ts))
    sql.append(" );")

    sql_cmd = ''.join(str(x) for x in sql)

    #print('InsertTransaction sql:', sql_cmd)
    cur.execute(sql_cmd)
    #print('Exit InsertTransaction')
    return True


def GetPosition(cur, id, ticker):
    #print('Enter GetPosition')
    # For a given id & ticker retrieve position
    position_id = -1
    agg_bal     = -1.0
    shares      = -1

    sql = "SELECT id, agg_bal, shares FROM positions " \
        + "WHERE user_id = " + str(id) + " AND ticker = '" + ticker + "';"

    #print('sql:', sql)

    cur.execute(sql)
    rows = cur.fetchall()

    #print('len(rows):', len(rows))

    if len(rows) > 0:
        # user already has a position, return it
        position_id = rows[0][0]
        agg_bal     = rows[0][1]
        shares      = rows[0][2]

    #print('Exit GetPosition')
    return position_id, agg_bal, shares

def UpdatePosition(cur, id, ticker, buy_or_sell, num_shares, last_price):
    # update position for buy or sell
    #print('Enter UpdatePosition')
    # get existing position.  if no position, position_id = -1
    existing_position_id, existing_agg_bal, existing_shares = GetPosition(cur, id, ticker)

    #print('ticker:', ticker)
    #print('  position_id:', existing_position_id)
    #print('  agg_bal:', existing_agg_bal)
    #print('  sharex:', existing_shares)

    if buy_or_sell == 'buy':
        # agg_bal doesn't change  only shares increase
        sql = ""
        if existing_position_id < 0:
            # no current position, insert this trade as position
            new_agg_bal = -1 * (num_shares * last_price)  # cash out on buy
            sql = "INSERT INTO positions ( user_id, ticker, agg_bal, shares) VALUES ("\
                + str(id) + ", '" + ticker + "', " + str(new_agg_bal) + ", " + str(num_shares) + " );"
        else:
            # add shares to existing shares & update position
            total_shares = existing_shares + num_shares
            new_agg_bal = existing_agg_bal - (num_shares * last_price)
            sql = "UPDATE positions " \
                + " SET shares = " + str(total_shares) \
                + ",   agg_bal = " + str(new_agg_bal) \
                + " WHERE user_id = " + str(id) \
                + " AND ticker = '" + ticker + "';"
        cur.execute(sql)
    elif buy_or_sell == 'sell':
        # inputs: id, ticker, buy_or_sell, num_shares, last_price
        # ticker lookup: existing_position_id, existing_agg_bal, existing_shares
        sql = ""
        new_shares = existing_shares - num_shares
        new_agg_bal = existing_agg_bal + (num_shares * last_price)
        sql = "UPDATE positions " \
            + " SET shares = " + str(new_shares) \
            + ",   agg_bal = " + str(new_agg_bal) \
            + " WHERE user_id = " + str(id) \
            + " AND ticker = '" + ticker + "';"
        cur.execute(sql)
    #print('Exit UpdatePosition')
    return 0

def SellStock(fname, id, stock, num_shares):

    con, cur = OpenConnection(fname)

    # get ticker and last price from web api
    ticker, name, exchange, last_price = GetLastPrice(stock)

    # validate user has stock to sell and enough shares to sell
    position_id, existing_agg_bal, existing_shares = GetPosition(cur, id, ticker)

    if position_id < 0:
        return -1     # can't sell something you don't own
    elif existing_shares < num_shares:
        return -2     # can't sell more than you've got
    else:
        # add to transactions
        InsertTransaction(cur, id, ticker, 'sell', num_shares, last_price)
        retSts = UpdatePosition(cur, id, ticker, 'sell', num_shares, last_price)

        # got some cash from this sale, update users.cash_left
        cur_cash = GetCurrentCash(cur, id)
        spend_amt = last_price * num_shares
        cash_left = cur_cash + spend_amt
        SetCurrentCash(cur, id, cash_left)

        con.commit()

    CloseConnection(con, cur)
    return retSts


def BuyStock(fname, id, stock, num_shares):
    # in order to buy stock the user must have enough cash on hand
    #print('Enter BuyStock')
    con, cur = OpenConnection(fname)

    # get current cash
    cur_cash = GetCurrentCash(cur, id)

    # get current stock last price
    ticker, name, exchange, last_price = GetLastPrice(stock)

    # if trying to buy more than cash we've got return -1
    spend_amt = last_price * num_shares
    if spend_amt > cur_cash:
        return -1

    # add to transactions
    InsertTransaction(cur, id, ticker, 'buy', num_shares, last_price)

    # update position
    UpdatePosition(cur, id, ticker, 'buy', num_shares, last_price)

    # cash_left is smaller with this buy, update users.cash_left
    cash_left = cur_cash - spend_amt
    SetCurrentCash(cur, id, cash_left)
    con.commit()

    CloseConnection(con, cur)
    #print('Exit BuyStock')
    return 0


def GetCurrentCash(cur, id):
    # for a given user.id return cash_left
    #print('Enter GetCurrentCash')
    sql = "SELECT cash_left FROM users where id = " + str(id)
    cur.execute(sql)
    rows = cur.fetchall()
    value = rows[0][0]
    amt = float(value)
    #print('Exit GetCurrentCash')
    return amt


def SetCurrentCash(cur, id, amt):
    # for a given user.id set cash_left
    #print('Enter SetCurrentCash')
    sql = "UPDATE users SET cash_left = " + str(amt) + " WHERE id = " + str(id)
    cur.execute(sql)
    #print('Exit SetCurrentCash')
    return True

def AddOrRemoveCash(fname, id, add_or_remove_flag, amt):
    tmp_amt = amt if add_or_remove_flag == 'A' else amt*-1

    con, cur = OpenConnection(fname)

    cur_amt = GetCurrentCash(cur, id)
    new_amt = cur_amt + tmp_amt
    retVal = []
    #print('tmp_amt:', tmp_amt,'cur_amt:', cur_amt, 'new_amt:', new_amt)
    if new_amt >= 0:
        # update users.cash_left
        result = SetCurrentCash(cur, id, new_amt)

        # insert cash transaction:
        #     ticker=CASH, xcn_type=buy or sell,
        #     num_shares=amt input and last_price=1.0
        xcn_type = 'buy' if tmp_amt > 0 else 'sell'
        InsertTransaction(cur, id, 'CASH', xcn_type, tmp_amt, 1.0)

        retVal.append(0)
        retVal.append(new_amt)
    else:
        # can't remove more cash than whats left in the account
        retVal.append(-1)
        retVal.append(0 if cur_amt < 0 else cur_amt)

    con.commit()
    CloseConnection(con, cur)

    # retVal is a list: [0] = status; [1] = cash amount after transaction
    return retVal


def GetAllUserIds(cur):
    # get list of unique users.id from database
    retVal = []
    cur.execute("""SELECT id FROM users GROUP BY id ORDER BY id;""")
    rows = cur.fetchall()
    for row in rows:
        retVal.append(row[0])
    return retVal


def GetPositions(fname, id, show_all_pos):
    # return list of tuples with:
    # users.id, users.cash_left, positions.ticker, positions.agg_bal, positions.shares
    retVal = []

    con, cur = OpenConnection(fname)

    # get list of users.id to get positions
    ids_to_get = []
    if show_all_pos == 'Y':
        ids_to_get = GetAllUserIds(cur)
    else:
        # only need to show positions for this user.id
        ids_to_get.append(id)

    # get cash & position info for each user id from database
    for uid in ids_to_get:
        sql = "SELECT u.id, u.initial_cash, u.cash_left, p.ticker, p.agg_bal, p.shares " \
            + " FROM users u " \
            + " LEFT JOIN positions p on u.id = p.user_id " \
            + " WHERE u.id = " + str(uid) + ";"
        #print('sql:', sql)
        cur.execute(sql)

        rows = cur.fetchall()
        for row in rows:
            pos_tuple = ( row[0], row[1], row[2], row[3], row[4], row[5] )
            retVal.append(pos_tuple)

    return retVal

    CloseConnection(con, cur)
