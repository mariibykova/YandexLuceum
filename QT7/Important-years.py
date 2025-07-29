
import sqlite3
dbname = input()
con = sqlite3.connect(dbname)
cur = con.cursor()
result = cur.execute("""SELECT films.year FROM films WHERE films.title LIKE 'Х%'""").fetchall()
 
used = []
for elem in result:
    if elem[0] not in used:
        print(elem[0])
        used.append(elem[0])
 
con.close()