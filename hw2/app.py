"""
A simple recipe list flask app
"""
import flask
from flask.views import MethodView
from RecipeBookMainPage import RecipeBookMainPage
from RecipeList import RecipeList

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=RecipeBookMainPage.as_view('RecipeBookMainPage'),
                 methods=["GET"])

app.add_url_rule('/RecipeList/',
                 view_func=RecipeList.as_view('RecipeList'),
                 methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
