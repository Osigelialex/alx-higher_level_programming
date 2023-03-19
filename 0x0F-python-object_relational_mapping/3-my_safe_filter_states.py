#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], port=3306, host="localhost",
                        passwd=argv[2], db=argv[3], charset="utf8")
    cursor = Cursor()
    cursor.execute("SELECT * FROM states WHERE LIKE %s ORDER BY \
    id", (argv[4],))
    states = cursor.fetchall()
    [print(state) for state in states]
    cursor.close()
    db.close()
