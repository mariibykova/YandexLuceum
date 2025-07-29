import sqlite3
 
array = []
db = sqlite3.connect(input())
cursor = db.cursor()
result = cursor.execute("""SELECT DISTINCT title FROM genres WHERE id 
IN (SELECT genre FROM films WHERE year > 2009 AND year < 2012)""")
for i in result:
    if i[0] not in array:
        array.append(i[0])
for i in array:
    print(i)
db.close()