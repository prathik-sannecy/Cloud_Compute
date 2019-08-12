from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
    
class EnterIngredients(MethodView):
    def get(self):
        return render_template('EnterIngredients.html') 

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to Get Foods page when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['ingredient1'], request.form['ingredient2'], request.form['ingredient3'])
        return redirect(url_for('GetFoods')) 
