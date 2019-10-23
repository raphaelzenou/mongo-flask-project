import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from scrap import amazscrap

app = Flask(__name__, template_folder='templates')

#mongo DB details:
mongo_pwd = os.environ.get('MONGOPWD')
mongo_dbname = 'price-tracker'
mongo_url = 'mongodb+srv://mongodb_admin:'+ mongo_pwd +'@cluster0-byamh.gcp.mongodb.net/'+ mongo_dbname +'?retryWrites=true&w=majority'
app.config["MONGO_URI"] = mongo_url


#Creating a PyMongo instance
mongo = PyMongo(app)

#Routes
@app.route('/')
# @app.route('/get_items_tracked')
def home_func():
	return render_template('items.html', items=mongo.db.items.find())

@app.route('/new-item')
def new_item_func():
	return render_template('new-item.html')
	# if request.method == "POST":
	# 	new_item_form = request.form

		# error_empty_fields = list()
		# for new_item_characteristic, value in new_item_form.items():
		# 	if value == "":
		# 		error_empty_fields.append(new_item_characteristic)

		# if error_empty_fields:
		# 	error_message = f"Missing fields for {', '.join(error_empty_fields)}"
		# 	return render_template('new-item.html', feedback=error_message)
		
		#getting the item's url to be used by the scraper
		# print(new_item_form['item-url'])
	# return redirect(url_for('new_item_conf_func'))

@app.route('/confirmation', methods=["GET", "POST"])
def new_item_conf_func():
	new_item_form = request.form
	item = amazscrap(new_item_form['item-url'])
	return item

if __name__=='__main__':
	# Environment variables set in heroku
	# app.run(debug=True)
	app.run(host=os.environ.get('IP'),
	port=int(os.environ.get('PORT')),
	debug=False)