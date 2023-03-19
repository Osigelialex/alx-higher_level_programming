#!/usr/bin/python3
'''
Displays all values in the states table of
hbtn_0e_0_usa when name matches argument
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                        db=sys.argv[3], name=sys.argv[4])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    states = c.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    c.close()
    db.close()
