#!/usr/bin/python3

""" script that takes in the name of a state as an argument
and lists all cities of that state."""

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
            SELECT cities.name
            FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cur.execute(query, (clmn_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row[0], end="" if row == query_rows[-1] else ', ')
    print()
    cur.close()
    db.close()
