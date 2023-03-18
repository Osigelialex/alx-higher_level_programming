#!/usr/bin/python3
'''
Displays all values in the states table of
hbtn_0e_0_usa when name matches argument
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = mySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3]
                    name=argv[4]
    cursor = conn.Cursor()
    query = "SELECT * FROM states WHERE name = {}".format(sys.argv[4])
    cursor.execute(query)
    [print(i) for i in cursor.fetchall()]
