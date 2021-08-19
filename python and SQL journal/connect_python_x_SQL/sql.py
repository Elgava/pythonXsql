import sqlite3

def create_table():
    connection = sqlite3.connect("data.db")
    connection.execute("CREATE table if not exists entries(content TEXT, date TEXT);")
    connection.close()