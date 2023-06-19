#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    query = """
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        FROM cities
        INNER JOIN states ON states.id=cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    result = cur.fetchone()[0]
    if result:
        print(result)
    else:
        print("")

    cur.close()
    db.close()
