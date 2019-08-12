from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import foodmodel
import requests
import json
import yelp_api_sample # code taken from https://github.com/Yelp/yelp-fusion/blob/master/fusion/python/sample.py 

length = 20

def getKey(file_name):
    """
    Returns: String of the API key from a specified file
    """
    with open(file_name) as f:
        key = f.readline().strip()
        print(key)
        return key



class GetRestaurants(MethodView):
    def get(self):
        """
        Gets the food and location from the backend storage. Using this information, it queries the Yelp API to find nearby restaurants with that food

        Returns: webpage to render
        """
        # Ge the food and location from storage
        model = foodmodel.get_model()
        foods = model.select()
        food = foods[-1][0] 
        location = foods[-1][1] 

        # Query Yelp for busineeses
        businesses = yelp_api_sample.search(getKey('yelp.key'), food, location)
        
        # Get the retaurant names
        restaurants = []
        i = 0
        while i < 5:
            try:
                restaurants.append({'name' : businesses.get("businesses")[i].get('alias')})
                i += 1
            except:
                break
        if i == 0:
            restaurants.append({'name' : "No foods found"})
        
        return render_template('RestaurantList.html', restaurants=restaurants)
