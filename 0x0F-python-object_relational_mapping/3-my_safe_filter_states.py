#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, writing one that is safe from MySQL injections!
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER by states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
