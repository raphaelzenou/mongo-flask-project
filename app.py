import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
from scrap import amazscrap

app = Flask(__name__, template_folder='templates')

#mongo DB details:
load_dotenv()
mongo_pwd = os.getenv('MONGOPWD')
mongo_dbname = 'price-tracker'
mongo_url = 'mongodb+srv://mongodb_admin:'+ mongo_pwd +'@cluster0-byamh.gcp.mongodb.net/'+ mongo_dbname +'?retryWrites=true&w=majority'
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

if __name__=='__main__':
	# Environment variables set in heroku
	app.run(debug=True)
	# app.run(host=os.environ.get('IP'),
	# port=int(os.environ.get('PORT')),
	# debug=False)