
#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves
all states with names starting with 'N', sorted by id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
