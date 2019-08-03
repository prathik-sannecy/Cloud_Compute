from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class RecipeList(MethodView):
    def get(self):
        model = gbmodel.get_model()
        recipes = model.select()
        return render_template('RecipeList.html', recipes=recipes)

