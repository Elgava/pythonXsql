# title, release_date, watched
import datetime
import sqlite3

Create_movies_table = """Create table if not exists movies (
    title Text,
    release_timeStamp REAL,
    watched Intereger
);"""

insert_movies = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_upcoming_movies = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_Watched_movies = "SELECT * FROM movies WHERE watched = 1;"
set_movie_watched = "UPDATE movies SET watched = 1 WHERE title = ?;"
delete_movie = "DELETE FROM movies WHERE title = ?;"

connection = sqlite3.connect("data.db")

def Create_tables():
    with connection:
        connection.execute(Create_movies_table)

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(insert_movies, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_upcoming_movies, (today_timestamp,))
            cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()

def watch_movie(title):
        with connection:
            connection.execute(set_movie_watched, (title),)

def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_Watched_movies)
        return cursor.fetchall()