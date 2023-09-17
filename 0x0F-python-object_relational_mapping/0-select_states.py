#!/usr/bin/python3

""" script that lists all states from the database """

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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()


# useing context manager the "with" to manage the closing of the DB conection
#  instead of closing it manually

# if __name__ == "__main__":
#     try:
#         mysql_username, mysql_password, mysql_db_name = args[1],\
#             args[2], args[3]
#         with MySQLdb.connect(
#             host='localhost',
#             port=3306,
#             user=mysql_username,
#             passwd=mysql_password,
#             db=mysql_db_name
#         ) as db:
#             with db.cursor() as cur:
#                 cur.execute("SELECT * FROM states ORDER BY id ASC")
#                 query_rows = cur.fetchall()
#                 for row in query_rows:
#                     print(row)

#     except MySQLdb.Error as err:
#         print("MySQL Error:", err)
