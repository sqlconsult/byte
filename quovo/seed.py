#!/usr/bin/env python3

import os
# import sys
# import sqlite3
# import time

import connection as conn


def seed_database(db_name):
    con, cur = conn.open_connection(db_name)

    cur.execute(
       """CREATE TABLE accounts (
              acct_id       INTEGER PRIMARY KEY AUTOINCREMENT,
              initial_limit NUMERIC(18,6),
              current_limit NUMERIC(18,6),
              created_on    REAL DEFAULT (datetime('now', 'localtime')) );
        """
        )

    cur.execute(
        """CREATE TABLE trans (
              trans_id       INTEGER PRIMARY KEY AUTOINCREMENT,
              acct_id        INTEGER,
              trans_type     VARCHAR(50),
              trans_amt      NUMERIC(18,6),
              created_on     REAL DEFAULT (datetime('now', 'localtime')) );
        """
        )

    cur.execute(
        """CREATE TABLE holds (
              hold_id        INTEGER PRIMARY KEY AUTOINCREMENT,
              acct_id        INTEGER,
              vendor_id      INTEGER,
              hold_amt       NUMERIC(18,6),
              created_on     REAL DEFAULT (datetime('now', 'localtime')) );
        """
        )

    # cur_time = time.time()
    sql = "INSERT INTO accounts ( initial_limit, current_limit ) " \
        + "VALUES ( 100000, 100000 );"
    cur.execute(sql)

    con.commit()

    conn.close_connection(con, cur)


def main():
    # Running from command line, create tables and seed database
    db_name = 'debit.db'
    if os.path.isfile(db_name):
        user_inp = input('Confirm re-creating database (y/n)?')
        if user_inp.upper() == 'Y':
            # delete it
            os.remove(db_name)
            print('Removed file: ', db_name)

    seed_database(db_name)
    print('Database created and seeded\nDone.')


if __name__ == '__main__':
    main()