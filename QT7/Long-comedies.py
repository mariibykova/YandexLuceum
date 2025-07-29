import sqlite3
db_name = input()
conor = sqlite3.connect(db_name)
nor = conor.cursor()
result = nor.execute('''SELECT title FROM Films 
            WHERE duration >= 60 AND genre=(
        SELECT id FROM genres
            WHERE title = 'комедия')''').fetchall()
for elem in result:
    print(elem[0])
conor.close()