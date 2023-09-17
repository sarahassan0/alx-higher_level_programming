#!/usr/bin/python3

""" script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv as args

if __name__ == "__main__":
    mysql_username, mysql_password, mysql_db_name, clmn_name = args[1],\
        args[2], args[3], args[4]
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
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC
            """.format(clmn_name)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
