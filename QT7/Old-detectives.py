import sqlite3


def get_detective_films(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    query = """SELECT title FROM Films
            WHERE (genre=(
SELECT id FROM genres
            WHERE title = 'детектив')) AND year BETWEEN 1995 AND 2000"""
    cursor.execute(query)
    films = cursor.fetchall()
    conn.close()
    for film in films:
        print(film[0])


if __name__ == "__main__":
    s = input()
    get_detective_films(s)
