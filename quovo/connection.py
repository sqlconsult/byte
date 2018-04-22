#!/usr/bin/env python3

import sys
import sqlite3


def close_connection(con, cur):
    try:
        cur.close()
        con.close()
        return 0
    except:
        print_error(sys.exc_info())


def open_connection(db_name):
    try:
        connection = sqlite3.connect(db_name, check_same_thread=False)
        cursor     = connection.cursor()
        return connection, cursor
    except:
        print_error(sys.exc_info())
        return 1, 1


def print_error(info):
    print('Unexpected error')
    print('        type:', info[0])
    print('       value:', info[1])
    print('   traceback:', info[2])