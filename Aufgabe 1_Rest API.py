from sqlite3.dbapi2 import Cursor
from flask import Flask, request, jsonify, make_response
import sqlite3

app = Flask(__name__)

def db_connection():

    conn = None
    try:
        conn = sqlite3.connect("movies.sqlite")
    except sqlite3.Error as e:
        print(e)

    return conn

  
@app.route("/movies",methods=["GET","POST","DELETE"])

def movies():
    conn = db_connection() #sets connection to sqlite db
    cursor = conn.cursor() #to use sql queries
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM movies")
        movies = [
            dict(title=row[0],genre = [1], year = [2])
            for row in cursor.fetchall()
        ]
        if movies is not None:
            return make_response(jsonify(movies),200)

    if request.method == "POST":
        new_title = request.form["title"]
        new_genre = request.form["genre"]
        year = request.form["year"]
        sql = """INSERT INTO movies (title, genre, year )
                 VALUES (?,?,?)""" #parametrized query
        
        cursor = conn.execute(sql, (new_title,new_genre,year))
        conn.commit()   
        return make_response("Movie {} added successfully".format(new_title),201)
    
    

@app.route("/movies/<title>",methods=["GET","PUT","DELETE"])
def each_movie(title):
    conn = db_connection()
    Cursor = conn.cursor()
    

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM movies where title=?",(title,))
        movie = cursor.fetchall()
        
        if movie is not None:
           return make_response(jsonify(movie))
        else:
           return "Movie not existent",205
    
    
        
    if request.method == "DELETE":
        sql = """ DELETE FROM movies WHERE title=? """
        conn.execute(sql, (title,))
        conn.commit()
        return "The movie with title: {} has been deleted.".format(title), 200

    


app.run(port=5000) 
