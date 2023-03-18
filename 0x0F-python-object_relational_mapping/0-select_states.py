#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
a script that lists all states
from the database
'''
if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
