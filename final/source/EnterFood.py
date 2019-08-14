from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import foodmodel
    
class EnterFood(MethodView):
    def get(self):
        return render_template('EnterFood.html') 

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to GetRestaurants when completed.
        """
        model = foodmodel.get_model()
        model.insert(request.form['food'], request.form['location'])
        return redirect(url_for('GetRestaurants')) 
