"""
A simple food flask app.
Data is stored in a SQLite database that looks something like the following:

+-------+----------+
| food  | location |
+=======+==========+
| Pizza | Seattle  |
+-------+----------+

This can be created with the following SQL (see bottom of this file):

    create table foods (food text, location text);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'foods.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from foods")
        except sqlite3.OperationalError:
            cursor.execute("create table foods (food text, location text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains food, location
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM foods")
        return cursor.fetchall()

    def insert(self, food, location):
        """
        Inserts entry into database
        :param food: String
        :param location: String
        :return: True
        """
        params = {'food': food, 'location': location}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into foods (food, location) VALUES (:food, "
                       ":location)", params)

        connection.commit()
        cursor.close()
        return True
