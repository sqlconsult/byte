#!/usr/bin/env python3.6

import sqlite3

def main(database_name):
    connection = sqlite3.connect(database_name, check_same_thread=False)
    cursor     = connection.cursor()

    cursor.execute(
        """CREATE TABLE btc (
               pk INT PRIMARY KEY AUTOINCREMENT,
               unix_time INT,
               last_price NUMERIC(18, 6),
               trade_volume NUMERIC(18, 8)
           );
        """
    return cursor, connection

if __name__ == '__main__':
    cur, conn = main('cryptocurrencies.db')
    cur.close()
    conn.close()
