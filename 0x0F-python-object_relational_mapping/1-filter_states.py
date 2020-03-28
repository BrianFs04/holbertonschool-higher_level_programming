#!/usr/bin/python3
'''
Script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states WHERE name  LIKE '%N%' "
                   "COLLATE Latin1_General_CS;")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db_connection.close()

if __name__ == '__main__':
    mysqlconnect()
