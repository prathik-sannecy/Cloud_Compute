from flask import render_template
from flask.views import MethodView
import gbmodel

class RecipeBookMainPage(MethodView):
    def get(self):
        return render_template('RecipeBookMainPage.html')
