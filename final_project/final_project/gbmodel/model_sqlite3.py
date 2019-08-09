"""
A simple ingredients flask app.
Data is stored in a SQLite database that looks something like the following:

+------------+------------------+------------------+
| Ingredient1| Ingredient2    | Ingredient3        |
+============+================+====================+
| Pasta      | Tomatoes       | Onions             |
+------------+----------------+--------------------+

This can be created with the following SQL (see bottom of this file):

    create table ingredient (ingredient1 text, ingredient2 text, ingredient3 text);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from ingredients")
        except sqlite3.OperationalError:
            cursor.execute("create table ingredients (ingredient1 text, ingredient2 text, ingredient3 text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains 3 ingredients
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ingredients")
        return cursor.fetchall()

    def insert(self, ingredient1, ingredient2, ingredient3):
        """
        Inserts entry into database
        :param ingredient1: String
        :param ingredient2: String
        :param ingredient3: String
        :return: True
        """
        params = {'ingredient1': ingredient1, 'ingredient2': ingredient2, 'ingredient3': ingredient3}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into ingredients (ingredient1, ingredient2, ingredient3) VALUES (:ingredient1, "
                       ":ingredient2, :ingredient3)", params)

        connection.commit()
        cursor.close()
        return True
