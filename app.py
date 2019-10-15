import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


#mongo DB details:
['MONGO_DBNAME'] = 'price-tracker' is now optional
mongo_pwd = os.environ.get('MONGOPWD')
mongo_url = 'mongodb+srv://mongodb_admin:' + mongo_pwd + '@cluster0-byamh.gcp.mongodb.net/test?retryWrites=true&w=majority'

app.config["MONGO_URI"] = mongo_url

#Creating a PyMongo instance
mongo = PyMongo(app)

app = Flask(__name__)

@app.route('/')
@app.route('/get_items_tracked')
def get_items_tracked():
	# return render_template('items.html', items=mongo.db.items.find())
	return mongo.db.items.find())

if __name__=='__main__':
	# Environment variables set in heroku
	app.run(host=os.environ.get('IP'),
	port=int(os.environ.get('PORT')),
	debug=True)