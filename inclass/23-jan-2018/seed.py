#!/usr/bin/env python3.6

import sqlite3

def main(database_name):
    connection = sqlite3.connect(database_name, check_same_thread=False)
    cursor     = connection.cursor()

    with open('', 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            timestamp = row[0] 
            last_price = row[1]
            trade_volume = row[2]

            cursor.execute(
                """INSERT INTO btc (unix_time, last_price, trade_volume ) VALUES
                   ({time}, {price}, {volume} );
                """.format( \
                    time   = row[0], \
                    price  = row[1], \
                    volume = row[2] )
                )
    return cursor, connection

if __name__ == '__main__':
    cur, conn = main('cryptocurrencies.db')
    conn.commit()
    cur.close()
    conn.close()
