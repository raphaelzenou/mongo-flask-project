import os
from flask import Flask

#mongo DB details:
#mongo_pwd = os.environ.get('MONGOPWD')
#mongo_url = 'mongodb+srv://mongodb_admin:' + mongo_pwd + '@cluster0-byamh.gcp.mongodb.net/test?retryWrites=true&w=majority'


app = Flask(__name__)

@app.route('/')
def hello():
	return 'Bonjour Heroku'

if __name__=='__main__':
	# Environment variables set in heroku
	app.run(host=os.environ.get('IP'),
	port=int(os.environ.get('PORT')),
	debug=True)