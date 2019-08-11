from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import foodmodel
import requests
import json
import yelp_api_sample # code taken from https://github.com/Yelp/yelp-fusion/blob/master/fusion/python/sample.py 

length = 20

def getKey(file_name):
    with open(file_name) as f:
        key = f.readline().strip()
        print(key)
        return key



class GetRestaurants(MethodView):
    def get(self):
        model = foodmodel.get_model()
        foods = model.select()
        food = foods[-1][0] 
        location = foods[-1][1] 


        businesses = search(getKey('yelp.key'), term, location)

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
        
        return render_template('RestaurantList.html', foods=foods)
