"""
Python list model
"""
from datetime import date
from .Model import Model


class model(Model):
    def __init__(self):
        self.recipes = []
        self.insert("Cereal", "Prathik", "Milk, Frosted Flakes", "2min", "Beginner",
                    "Put Frosted Flakes in the bowl. Then add milk")
        self.insert("Sandwich", "Chet", "Bread, Tomatoes, Olives, Lettuce, mustard", "10min", "Medium",
                    "Place the tomatoes, olives, lettuce, and mustard onto one slice of bread. Then put the other "
                    "slice on top")
        self.insert("Pasta", "Dennis", "Pasta, Pasta Sauce, Onions, Bell Pepper", "15min", "Expert",
                    "Boil the pasta for 10min. Stir Fry the Onions and Bell Pepper for 10min. Mix the pasta "
                    "with the vegetables. Add the pasta sauce and let it simmer for 2min")

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
