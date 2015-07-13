import os
from flask.ext.httpauth import HTTPBasicAuth

from flask_restful import Api
from flask import Flask, render_template, make_response

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'you-will-never-guess'


auth = HTTPBasicAuth()
api = Api(app)


@app.route("/")
def index():
	return render_template("home.html")


@app.errorhandler(404)
def not_found(error):
	return make_response(render_template("404.html"))


@app.errorhandler(409)
def not_found(error):
	return make_response(render_template("409.html"))


@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
	return response


# import routes
from app import controllers
