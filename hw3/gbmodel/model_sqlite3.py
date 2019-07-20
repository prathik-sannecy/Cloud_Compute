"""
A simple recipelist flask app.
ata is stored in a SQLite database that looks something like the following:

+------------+------------------+------------------+----------------+----------------+
| Title      | Author           | Ingredients      | Time Taken     | Skill Level    |
+============+==================+==================+----------------+----------------+
| Pasta      | John Watts       | Tomatoes, Onions | 10min          | Intermediate   |
+------------+------------------+------------------+----------------+----------------+

This can be created with the following SQL (see bottom of this file):

    create table recipelist (title text, author text, ingredient text, time text, skill text, description text);

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
            cursor.execute("select count(rowid) from recipelist")
        except sqlite3.OperationalError:
            cursor.execute("create table recipelist (title text, author text, ingredient text, time text, skill text, "
                           "description text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM recipelist")
        return cursor.fetchall()

    def insert(self, title, author, ingredient, time, skill, description):
        """
        Inserts entry into database
        :param title: String
        :param author: String
        :param ingredient: String
        :param time: String
        :param skill: String
        :param description: String
        :return: True
        """
        params = {'title': title, 'author': author, 'ingredient': ingredient, 'time': time, 'skill': skill, 'description': description}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into recipelist (title, author, ingredient, time, skill, description) VALUES (:title, "
                       ":author, :ingredient, :time, :skill, :description)", params)

        connection.commit()
        cursor.close()
        return True
