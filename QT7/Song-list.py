import sqlite3

a = input()
con = sqlite3.connect('music_db.sqlite')

cur = con.cursor()

resul = cur.execute("""
SELECT DISTINCT Name FROM Track WHERE
Albumid IN (SELECT Albumid FROM Album WHERE Artistid IN
(SELECT Artistid FROM Artist WHERE Name = ?))
""", (a,)).fetchall()
resul = sorted(set(resul))
for elem in resul:
    print(elem[0])
con.close()