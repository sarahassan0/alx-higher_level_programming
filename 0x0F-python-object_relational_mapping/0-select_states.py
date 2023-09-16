#!/usr/bin/python3

""" script that lists all states from the database """

import MySQLdb
from sys import argv as args

if __name__ == "__main__":
    mysql_username, mysql_password, mysql_db_name = args[1], args[2], args[3]
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_db_name
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
