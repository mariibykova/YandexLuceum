import sqlite3

a = []
genre = input()
db = sqlite3.connect("music_db.sqlite")
cur = db.cursor()
result = cur.execute(
    f"""SELECT DISTINCT a.name
FROM genre g, track t, album al, artist a
WHERE t.genreid = g.genreid 
AND t.albumid = al.albumid
AND al.artistid = a.artistid
AND g.name = '{genre}'
ORDER BY a.name;"""
)
for i in result:
    if i[0] not in a:
        a.append(i[0])
for i in a:
    print(i)
db.close()
