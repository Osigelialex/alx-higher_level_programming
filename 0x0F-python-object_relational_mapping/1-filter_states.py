#!/usr/bin/python3
'''
Lists all states from database starting
with an N
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%'"
    cursor.execute(query)
    [print(i) for i in cursor.fetchall()]
