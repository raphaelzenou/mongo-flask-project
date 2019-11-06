# Standard or External packages
import os
import sys
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, flash
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

# Setting secret key for sessions (here mainly flash messages)
app.secret_key = os.getenv('SECRET_KEY')


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

# *** ROUTES *** 

@app.route('/')
def home_func():
	return render_template('home.html', 
	users = mongo.db.users.find())

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
	proxy_or_not = new_item_form['proxy']
	user = {'user_name' : new_item_form['user_name']}

	if 'amazon' in new_item_form['item_url']:
		try:
			item = amazscrap(new_item_form['item_url'], proxy_or_not)

			if item['item_short_title'] == 'SCRAPER_BLOCKED_BY_AMAZON':

				e = 'Amazon blocked the scraper. \
				Please try clearing your browsing data and if you can \
				also change your IP address with a VPN.\
				You can also simply try using the proxy option provided.\
				Apologies for the inconvenience but Amazon is fighting hard\
				to prevent us from scraping their product pages...'
				return render_template('error.html', 
				error=e, user=user)
			else:
				return render_template('item-confirmation.html', 
				item=item, user=user)
		except:
			e = sys.exc_info()[1]
			return render_template('error.html', 
			error=e, user=user)
	else:
		e = 'You seem to not be using an Amazon product page link.'
		return render_template('error.html', 
		error=e, user=user)

@app.route('/add', methods=["POST"])
def add_item():
	new_item_form_ok = request.form.to_dict()
	# to_dict method changes the ImmutableMultiDict
	# type of request.form
	# so we can add the date below to it and it will work with MongoDB

	if new_item_form_ok['item_title'] == 'N/A':
		new_item_form_ok['item_title'] = new_item_form_ok['item_short_title']

	try:
		mongo.db.items.update(
			{'_id' : ObjectId(new_item_form_ok['_id'])},
			{
				'item_short_title' : new_item_form_ok['item_short_title'],
				'item_title' : new_item_form_ok['item_title'],
				'item_category' : new_item_form_ok['item_category'],
				'item_currency' : new_item_form_ok['item_currency'],
				'item_price_float' : new_item_form_ok['item_price_float'],
				'item_url' : new_item_form_ok['item_url'],
				'item_image_main_link' : new_item_form_ok['item_image_main_link'],
				'user_name' : new_item_form_ok['user_name'],
			},
			upsert=True)
		flash(u'Item updated!', 'info')

	# When it is a new object and there is no '_id'
	# Simply insert
	except:
		new_item_form_ok['date_added'] = datetime.today()
		mongo.db.items.insert_one(new_item_form_ok)
		flash(u'New item added!', 'info')
	


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
	item = mongo.db.items.find_one({'_id': ObjectId(item_id)})
	user_name = item['user_name']
	
	mongo.db.items.remove({'_id': ObjectId(item_id)})
	flash(u'Item deleted', 'info')
	return redirect(url_for('items', user = user_name))

# Editing Item
@app.route('/edit/<item_id>')
def edit_item(item_id):
	item_details = mongo.db.items.find_one({'_id': 
	ObjectId(item_id)})
	user_details =  {'user_name' : item_details['user_name']}

	return render_template('item-confirmation.html', 
	item = item_details,
	user = user_details)





# Running the app
if __name__=='__main__':
	app.run(host=os.getenv('IP'),
	port=int(os.getenv('PORT')),
	debug=True)
