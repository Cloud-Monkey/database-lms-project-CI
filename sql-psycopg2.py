import psycopg2

# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - select "name" records from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select "Queen" "Name" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s ', ["Queen"])

# query 4 - select "ArtistId" 51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s ', [51])

# query 5 - select "ArtistId" 51 from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s ', [51])

# query 6 - select all records where the composer is "Queen" from the "Tracks" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s ', ["Queen"])


# fetch results (multiple)
results = cursor.fetchall()

# fetch results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)

