#!/usr/bin/python3

""" lists all states with a name starting with N (upper N) from database """

import MySQLdb
from sys import argv as args

if __name__ == "__main__":
    mysql_username, mysql_password, mysql_db_name = args[1],\
        args[2], args[3]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_db_name
    )
    cur = db.cursor()
    query = """
            SELECT * FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY id ASC
            """
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
