import sqlite3
a = input()
con = sqlite3.connect(a)
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films
            WHERE duration <= 85""").fetchall()
 
for elem in result:
    print(*elem)
con.close()