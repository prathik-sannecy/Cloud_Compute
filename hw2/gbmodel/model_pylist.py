"""
Python list model
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.recipes= []

    def select(self):
        """
        Returns guestentries list of lists
        Each list in guestentries contains: name, email, date, message
        :return: List of lists
        """
        return self.recipes

    def insert(self, title, author, ingredient, time, skill, description):
        """
        Appends a new list of values representing new message into guestentries
        :param name: String
        :param email: String
        :param message: String
        :return: True
        """
        params = [title, author, ingredient, time, skill, description]
        self.recipes.append(params)
        return True
