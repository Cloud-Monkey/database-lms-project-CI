from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions for our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table (
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table (
    "Name", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String)
)

# making the connection
with db.connect() as connection:
