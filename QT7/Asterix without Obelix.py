import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT films.title FROM films
 WHERE title LIKE "%Астерикс%" AND title NOT LIKE "%Обеликс%" """).fetchall()
for elem in result:
    print(elem[0])
con.close()