from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import requests
import json

length = 20

def getKey(file_name):
    with open(file_name) as f:
        key = f.readline().strip()
        print(key)
        return key

def getUrl(url):
    res = requests.get(url)
    res_content = res.content
    json_data = json.loads(res_content)
    return json_data


class GetFoods(MethodView):
    def get(self):
        model = gbmodel.get_model()
        ingredients = model.select()
        ingredient1 = ingredients[-1][0] 
        ingredient2 = ingredients[-1][1] 
        ingredient3 = ingredients[-1][2] 
        url = "https://api.nal.usda.gov/ndb/search/?format=json&q=" + ingredient1 + " " + ingredient2 + " " + ingredient3 + "&sort=n&max=25&offset=0&api_key="+getKey("datagov.key")
        getFoods = getUrl(url)
        try:
            foods = [{'name' : getFoods.get("list").get("item")[i].get("name")} for i in range(0, len(getFoods.get("list").get("item")))]
        except:
            foods = [{'name' : "No foods found"}]
        return render_template('FoodList.html', foods=foods)
        #return redirect(url_for('Food Finder'))
