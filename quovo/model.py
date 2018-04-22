#!/usr/bin/env python3

import connection as conn


def charge(acct_id, amt, db_name):
    """
    :param acct_id:       Account number to charge
    :param amt:           Amount to charge
    :param db_name:       Database name (path)
    :return:              0  = Success
                          -1 = Charge failed (database error)
                          -2 = Insufficient funds
    """
    try:
        # Get connection and cursor to database
        con, cur = conn.open_connection(db_name)

        ret_sts = debit_acct(cur, acct_id, amt, 'charge')

        # Commit all database transactions and close database connection
        con.commit()
        conn.close_connection(con, cur)

        return ret_sts
    except Exception as e:
        print(e)
        return -1


def create_account(initial_balance, db_name):
    """
    :param initial_balance: Initial balance for this account
    :param db_name:         Database name (path)
    :return:                -1 on failure or new account number
    """
    #
    # For a given initial balance create a new account
    #
    try:
        # Get connection and cursor to database
        con, cur = conn.open_connection(db_name)

        # Build sql to insert this user
        sql = 'INSERT INTO accounts ( initial_limit, current_limit ) VALUES ( {0}, {0} );'.format(initial_balance)

        # Insert into database and commit
        cur.execute(sql)

        # New account number = MAX(accounts.acct_id)
        new_acct_id = get_last_account_id(cur)

        insert_trans(cur, new_acct_id, 'create', initial_balance)

        # Commit all database transactions and close database connection
        con.commit()
        conn.close_connection(con, cur)
    except Exception as e:
        print(e)
        new_acct_id = -1

    return new_acct_id


def debit_acct(cur, acct_id, amt, action):
    """
    :param cur:     Open database cursor
    :param acct_id: Account id to act on
    :param amt:     Transaction amount
    :param action:  Action { 'charge' | 'hold' }
    :return:         0 = success
                    -1 = database error
                    -2 = insufficient funds
    """
    try:
        # For a given account, get current limit
        cur_limit = get_current_limit(cur, acct_id)

        # sufficient funds for this charge?
        if amt <= cur_limit:
            # yes, update current limit and enter a transaction
            trans_amt = cur_limit - amt
            ret_sts = set_current_limit(cur, acct_id, trans_amt)
            insert_trans(cur, acct_id, action, trans_amt)
            return ret_sts
        else:
            # no, return code for insufficient funds
            ret_sts = -2    # Insufficient funds
        return ret_sts
    except Exception as e:
        print(e)
        return -1


def get_current_limit(cur, acct_id):
    """
    :param cur:      Open database cursor
    :param acct_id: Account number to act on
    :return:         Current limit for this account
    """
    #
    # for a given account number get current limit
    #
    sql = 'SELECT current_limit FROM accounts WHERE acct_id = {acct_id}'.\
        format(acct_id=acct_id)
    cur.execute(sql)
    rows = cur.fetchall()
    current_limit = rows[0][0]
    return float(current_limit)


def get_last_account_id(cur):
    """
    :param cur: Open database cursor
    :return:    Last (maximum) accounts.acct_id
    """
    # gets maximum (last) user.id from database
    # using open connection and cursor
    sql = 'SELECT MAX(acct_id) AS MaxAcctNum FROM accounts;'
    cur.execute(sql)
    rows = cur.fetchall()
    acct_id = rows[0][0]
    return int(acct_id)


def hold(acct_id, vendor_id, amt, db_name):
    """
    :param acct_id:    Account id
    :param vendor_id:  Vendor id
    :param amt:        Hold amount
    :param db_name:    Database name (path)
    :return:           True on success
    """
    try:
        # Get connection and cursor to database
        con, cur = conn.open_connection(db_name)

        # Only 1 hold allowed per vendor id per account id
        sql = 'SELECT COUNT(*) FROM holds WHERE acct_id = {0} AND vendor_id = {1}'.\
            format(acct_id, vendor_id)
        cur.execute(sql)
        rows = cur.fetchall()
        num_holds = rows[0][0]

        if num_holds > 0:
            return -3

        sql = 'INSERT INTO holds (acct_id, vendor_id, hold_amt) VALUES'\
              '( {0}, {1}, {2} );'.format(acct_id, vendor_id, amt)

        # Insert hold into database
        cur.execute(sql)

        # Place a hold on this account for the amount specified
        ret_sts = debit_acct(cur, acct_id, amt, 'hold')
        if ret_sts < 0:
            return ret_sts

        # Commit all database transactions and close database connection
        con.commit()
        conn.close_connection(con, cur)

        return ret_sts
    except Exception as e:
        print(e)
        return -1


def insert_trans(cur, acct_id, action, trans_amt):
    """
    :param cur:       Open database cursor
    :param acct_id:   Account number
    :param action:    Action { 'create' | 'charge' | 'hold' | 'settle' }
    :param trans_amt: Transaction amount
    :return:          True on success
    """
    # build sql to insert this user
    sql = "INSERT INTO trans ( acct_id, trans_type, trans_amt ) " \
          "VALUES ( {0}, '{1}', {2} );".format(acct_id, action, trans_amt)

    # insert into database and commit
    cur.execute(sql)
    return True


def set_current_limit(cur, acct_id, new_limit):
    """
    :param cur:       Open database cursor
    :param acct_id:   Account number to act on
    :param new_limit:
    :return:
    """
    #
    # for a given account number set a new current limit
    #

    # build sql to update current limit
    print(acct_id, new_limit)
    sql = 'UPDATE accounts SET current_limit = {current_limit} WHERE acct_id = {acct_id}'.\
        format(current_limit=new_limit, acct_id=acct_id)

    # insert into database and commit
    cur.execute(sql)
    return 0


def release_hold(acct_id, vendor_id, cur):
    """
    :param acct_id:     Account id to act on
    :param vendor_id:   Vendor  id to act on
    :param cur:         Open database cursor
    :return:            True on success, else False
    """
    try:
        # Is there a hold to release?
        sql = 'SELECT COUNT(*) AS NumHolds, SUM(hold_amt) AS Amt FROM holds WHERE acct_id = {0} AND vendor_id = {1}'. \
            format(acct_id, vendor_id)
        cur.execute(sql)
        rows = cur.fetchall()
        num_holds = rows[0][0]

        # Any holds to release?
        if num_holds == 0:
            return True    # No, successful

        # Save hold amount before deleting hold to credit back to account
        hold_amt = int(rows[0][1])

        print(num_holds, hold_amt)

        # update account limit by adding these funds bak
        current_limit = get_current_limit(cur, acct_id)
        new_limit = current_limit + hold_amt
        set_current_limit(cur, acct_id, new_limit)

        # Release the hold by deleting it from the database
        sql = 'DELETE FROM holds WHERE acct_id = {0} AND vendor_id = {1}'. \
            format(acct_id, vendor_id)

        # Remove hold from database
        cur.execute(sql)

        # Insert settle hold transaction
        insert_trans(cur, acct_id, 'settle', hold_amt)

        return True
    except Exception as e:
        print(e)
        return False


def settle_hold(acct_id, vendor_id, new_amt, db_name):
    try:
        # Get connection and cursor to database
        con, cur = conn.open_connection(db_name)

        # Release hold even if charge is declined
        release_hold(acct_id, vendor_id, cur)
        con.commit()

        # Issue charge to account for this new amount
        ret_sts = debit_acct(cur, acct_id, new_amt, 'settle')
        con.commit()
        return ret_sts
    except Exception as e:
        print(e)
        return -1
