import sqlite3

name = input()
con = sqlite3.connect(name)
cur = con.cursor()
result = cur.execute(
    """SELECT films.title FROM films WHERE films.title LIKE '%?'"""
).fetchall()
for elem in result:
    print(elem[0])

con.close()
