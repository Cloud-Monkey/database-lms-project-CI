from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions for our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for artist table
artist_table = Table (
    "Artist", meta,
)

# making the connection
with db.connect() as connection:
