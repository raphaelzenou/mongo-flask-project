# Standard or External packages
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Own packages
from scrap import amazscrap

app = Flask(__name__, template_folder='templates')

# Activating the use of .env file containing Environment variables
load_dotenv() 
# .env is in the .gitignore file for security reasons
# Environment variables are then accessed with os.getenv(<var>)
# Heroku will then be able to access its own environment variables
# with the same command
# initialisation can even be used using these Heroku env var
# with the command 'heroku config -s >> .env'


# MongoDB details:
mongo_login = os.getenv('MONGOLOGIN')
mongo_pwd = os.getenv('MONGOPWD')
mongo_dbname = os.getenv('MONGODBNAME')
mongo_url = 'mongodb+srv://' + mongo_login + ':'+ mongo_pwd +'@cluster0-byamh.gcp.mongodb.net/'+ mongo_dbname +'?retryWrites=true&w=majority'
app.config["MONGO_URI"] = mongo_url

#Creating a PyMongo instance
mongo = PyMongo(app)

#Routes
@app.route('/')
def home_func():
	return render_template('items.html', items=mongo.db.items.find())

@app.route('/new-item')
def new_item_func():
	return render_template('new-item.html')

@app.route('/confirmation', methods=["GET", "POST"])
def new_item_conf_func():
	new_item_form = request.form
	item = amazscrap(new_item_form['item-url'])
	return render_template('new-item-confirmation.html', item=item)

# Running the app
if __name__=='__main__':
	app.run(host=os.getenv('IP'),
	port=int(os.getenv('PORT')),
	debug=False)
