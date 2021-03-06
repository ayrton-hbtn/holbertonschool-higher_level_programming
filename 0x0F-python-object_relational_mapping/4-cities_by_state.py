#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa """


if __name__ == "__main__":
    import MySQLdb
    import sys
    argv = sys.argv
    server = MySQLdb.Connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2],
                             db=argv[3], charset="utf8")
    cur = server.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states ON\
                states.id = cities.state_id ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    server.close()
