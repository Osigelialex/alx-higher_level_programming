#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM `states`")
    [print(i) for i in cursor.fetchall()]
