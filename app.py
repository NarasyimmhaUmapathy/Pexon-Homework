from flask import Flask, request, jsonify, wrappers
from typing import Union
import sqlite3

app = Flask(__name__)

def db_connection():

    conn = None
    try:
        conn = sqlite3.connect("movies.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn

# From Python 3.* on you can use typings to show what kind of variables are you using
@app.route("/movies", methods=["GET", "POST"])
def movies() -> wrappers.Response:
    
    try:
        conn = db_connection()
    except Exception as e:
        raise Exception("Not possible to establish a connection")
    
    if conn is not None:
        cursor = conn.cursor()
    
        if request.method == "GET":
            cursor = conn.execute("SELECT * FROM movies")
            books = [
                dict(id=row[0], title=row[1],genre = [2], year = [3])
                for row in cursor.fetchall()
            ]

            if movies is not None:
                return jsonify(books) 

        if request.method == "POST":
            if request.json is not None:
                # The data shall be defined as a list of objects
                for obj in request.json:
                    new_title = obj["title"]
                    new_genre = obj["genre"]
                    year = obj["year"]
                    
                    # (Comments should go above the code) parametrized query
                    sql = """INSERT INTO movies (title, genre, year)
                            VALUES (?,?,?)""" 
        
                    cursor = conn.execute(sql, (new_title, new_genre, year))
                conn.commit()
        
            # Better always return a JSON
            return jsonify({"result":"Movies added successfully"})

    return jsonify({"result": "Another response"})