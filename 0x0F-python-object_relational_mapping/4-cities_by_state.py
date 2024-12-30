#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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
    match = sys.argv[4]
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.states_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
