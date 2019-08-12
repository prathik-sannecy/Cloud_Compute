from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import requests
import json

length = 20

def getKey(file_name):
    with open(file_name) as f:
        key = f.readline().strip()
        print(key)
        return key

def get(url):
    res = requests.get(url)
    res_content = res.content
    json_data = json.loads(res_content)
    return json_data

url = "https://api.nal.usda.gov/ndb/search/?format=json&q=butter&sort=n&max=25&offset=0&api_key="+getKey("datagov.key")

get_url = get(url)

for i in range(0, length):
    print(get_url.get("list").get("item")[i].get("name"))

