from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class IngredientList(MethodView):
    def get(self):
        model = gbmodel.get_model()
        ingredients = [dict(ingredient1=row[0], ingredient2=row[1], ingredient3=row[2])
                   for row in model.select()]
        return render_template('IngredientList.html', ingredients=ingredients)

