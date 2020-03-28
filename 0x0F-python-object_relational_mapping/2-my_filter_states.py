#!/usr/bin/python3
'''
Script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
'''
import MySQLdb
import sys


def mysqlconnect():
    db_connection = None
    db_connection = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}'"
                   " COLLATE Latin1_General_CS;"
                   .format(sys.argv[4]))
    states = cursor.fetchone()

    print(states)

    cursor.close()
    db_connection.close()

if __name__ == '__main__':
    mysqlconnect()
