from flask import render_template
from flask.views import MethodView
import gbmodel

class FoodFinderMainPage(MethodView):
    def get(self):
        return render_template('FoodFinderMainPage.html')
