"""
Python list model
"""
from datetime import date
from .Model import Model


class model(Model):
    def __init__(self):
        self.recipes = []

    def select(self):
        """
        Returns recipes list of dictionary
        Each list in recipes contains: title, author, ingredient, time, skill, description
        :return: List of dictionary
        """
        return self.recipes

    def insert(self, title, author, ingredient, time, skill, description):
        """
        Appends a new dictionary of values representing new message into recipes
        :param title: String
        :param author: String
        :param ingredient: String
        :param time: String
        :param skill: String
        :param description: String
        :return: True
        """
        parameters = {}
        parameters['title'] = title
        parameters['author'] = author
        parameters['ingredient'] = ingredient
        parameters['time'] = time
        parameters['skill'] = skill
        parameters['description'] = description

        self.recipes.append(parameters)
        return True
