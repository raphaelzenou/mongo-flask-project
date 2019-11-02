# Standard or External packages
import os
import sys
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Own packages
from scrap import amazscrap

# creating the app
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
mongo_url = 'mongodb+srv://' + mongo_login + ':'+ mongo_pwd \
+'@cluster0-byamh.gcp.mongodb.net/'\
+ mongo_dbname +'?retryWrites=true&w=majority'
app.config["MONGO_URI"] = mongo_url

#Creating a PyMongo instance
mongo = PyMongo(app)

#Routes
@app.route('/')
def home_func():
	return render_template('home.html', 
	users = mongo.db.users.find())

# @app.route('/new-item')
# def new_item_func():
# 	return render_template('new-item.html', 
# 	users = mongo.db.users.find())

@app.route('/new-item/<selected_user>')
def new_item_func(selected_user):
	if selected_user == '#':
		return render_template('new-item.html', 
		users = mongo.db.users.find(), new_user = True)
	else:
		return render_template('new-item.html', 
		users = selected_user, new_user = False)

@app.route('/confirmation', methods=["POST"])
# GET is defaulted so no need to add it
def new_item_conf_func():
	new_item_form = request.form
	try:
		item = amazscrap(new_item_form['item_url'])
		user = {'user_name' : new_item_form['user_name']}	
		return render_template('new-item-confirmation.html', 
		item=item, user=user)
	except:
		e = sys.exc_info()[1]
		return render_template('error.html', error=e)

@app.route('/add', methods=["POST"])
def add_item():
	new_item_form_ok = request.form.to_dict()
	# to_dict method changes the ImmutableMultiDict
	# type of request.form
	# so that we can add the date below to it and it will work with MongoDB
	new_item_form_ok['date_added'] = datetime.today()
	mongo.db.items.insert_one(new_item_form_ok)

	# Adding user to MongoDB only if not already in the collection
	# This is made possible using upsert=True
	mongo.db.users.update(
		{'user_name' : new_item_form_ok['user_name']},
		{'$setOnInsert' : 
		{'user_name' : new_item_form_ok['user_name'],
		'date_added' : datetime.today()}},
		upsert=True)
	
	return redirect(url_for('items', 
	user = new_item_form_ok['user_name'] ))

# Deleting item and then routing to the user page
@app.route('/delete/<item_id>')
def delete_item(item_id):
	user_name = mongo.db.items.find_one({'_id': 
	ObjectId(item_id)})['user_name']
	
	mongo.db.items.remove({'_id': ObjectId(item_id)})
	return redirect(url_for('items', user = user_name))

# Users filtering happens in two steps
# 1 - username is retrieved from the form
@app.route('/user_filter', methods=["POST"])
def user_filter():
	user_selection_form = request.form
	user_name = user_selection_form['user_name']
	return redirect(url_for('items', user = user_name))

# 2- we use this username to create a bespoke route
# to the user page
@app.route('/items/<user>')
def items(user):
	return render_template('items.html', 
	items=mongo.db.items.find({'user_name' : user}), 
	active_user = user,
	users = mongo.db.users.find())


# Running the app
if __name__=='__main__':
	app.run(host=os.getenv('IP'),
	port=int(os.getenv('PORT')),
	debug=True)
