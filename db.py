import sqlite3

conn = sqlite3.connect("movies.sqlite")

cursor = conn.cursor()
sql_query = """ 
        CREATE TABLE movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    genre  TEXT NOT NULL,
                    year INTEGER NOT NULL
                    )
        """
cursor.execute(sql_query)
