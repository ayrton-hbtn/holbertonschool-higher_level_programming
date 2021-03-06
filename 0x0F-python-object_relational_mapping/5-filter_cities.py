#!/usr/bin/python3
""" takes in the name of a state as arg and lists all cities of that state """


if __name__ == "__main__":
    import MySQLdb
    import sys
    argv = sys.argv
    server = MySQLdb.Connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2],
                             db=argv[3], charset="utf8")
    cur = server.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                ON states.id = cities.state_id\
                AND states.name = %s ORDER BY cities.id ASC", [argv[4]])
    query_rows = cur.fetchall()
    i = len(query_rows)
    for j in range(i - 1):
        print(f"{query_rows[j][0]}, ", end="")
    if (i != 0):
        print(f"{query_rows[j + 1][0]}")
    else:
        print()
    cur.close()
    server.close()
