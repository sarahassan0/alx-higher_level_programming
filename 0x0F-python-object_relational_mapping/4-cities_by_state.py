#!/usr/bin/python3

""" script that lists all cities from the database hbtn_0e_4_usa."""

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
            SELECT cities.id, cities.name, states.name
            FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
