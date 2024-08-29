import psycopg2

# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "artist" table
cursor.execute('SELECT * FROM "Artist"')

# query 2 - select "name" records from the "artist" table
cursor.execute('SELECT "Name" FROM "Artist"')

# fetch results (multiple)
results = cursor.fetchall()

# fetch results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)

