import sqlite3
 
result = sqlite3.connect('music_db.sqlite').cursor().execute(
    f"""SELECT DISTINCT Album.Title FROM Album
    INNER JOIN Track ON Album.AlbumId = Track.AlbumId
    INNER JOIN Genre ON Genre.GenreId = Track.GenreId
    INNER JOIN Artist ON Artist.ArtistId = Album.ArtistId
WHERE Genre.Name = ?
ORDER BY Artist.ArtistId, Album.Title""", (input(),))
for elem in result:
    print(*elem)

