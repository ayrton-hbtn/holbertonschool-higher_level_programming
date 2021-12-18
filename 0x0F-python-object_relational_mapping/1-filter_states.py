#!/usr/bin/python3
""" lists all states with a name starting with N from the db hbtn_0e_0_usa """

if __name__ == "__main__":
    import MySQLdb
    import sys
    argv = sys.argv
    server = MySQLdb.Connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2],
                             db=argv[3], charset="utf8")
    cur = server.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    server.close()
