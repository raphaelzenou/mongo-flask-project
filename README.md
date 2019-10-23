# Price Tracker for Amazon with value storage

Price Tracker is an app where users can add amazon links and track the price of the items they like.
Historical prices are then stored in a noSQL MongoDB Atlas database so users can have a look at the trends .

The idea is to combine Python's Beautiful Soup web scrapper with the Flask mini framework and Mongo DB (using PyMongo) in the Back End and Materialize in the Front End.
Hosting will be powered by Heroku connected with GitHub (not Heroku Git) for delployments.

## UX

Users will be able to add an amazon link via a form and then add the concerned item to their tracked products.
Users will also be able to edit, delete entries to offer them the full CRUD experience.

Users will have access to all their entries and will be able to see wether the current price is the lowest since they started tracking a product so as to help them make a decision on whether now is a good time to buy it.

Front end design will be done using Materialize

Optional features to potentially be added to make the UX even better:     
- a user login system is not required for the project, but I am thinking of adding one if time permits)
- an email alert system using Gmail's SMTP

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features

- Create : Users will be able to add an amazon link via a form and then add the concerned item to their tracked products.
- Read : Users will have access to all their entries and will be able to see wether the current price is the lowest since they started tracking a product so as to help them make a decision on whether now is a good time to buy it.
- Update / Delete : Users will also be able to edit, delete entries to offer them the full CRUD experience.

### Features Left to Implement
- Login system:  a user login system is not required for the project, but I am thinking of adding one if time permits).
- Email alerts: an email alert system using Gmail's SMTP.
- CRON : runs on UNIX (equivalent to Django CRON)
https://pythonprogramming.net/crontab-tutorial-basics/

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- Python 3.7.0
    * https://www.python.org/
- Flask 1.1.1 our Python web framework
    * https://palletsprojects.com/p/flask/ 
- Flask-PyMongo 2.3.0 to Interact with our MongoDB Atlas noSQL database
    * https://pypi.org/project/Flask-PyMongo/ 
- Requests 2.22.0
    * Used to get information from websites using HTTP requests
    * https://requests.kennethreitz.org/en/master/
- Beautifulsoup4  4.8.1 for Web Scraping
    * Used to parse website code obtained using the Requests library
    * https://pypi.org/project/beautifulsoup4/ 
- Materialize CSS Framework 
    * https://materializecss.com/
- ReCaptcha
    * https://techmonger.github.io/5/python-flask-recaptcha/ 

Technologies considered but not used :
- Flask Bootstrap for an easier Bootstrap integration notably with the WTF package
    * https://pythonhosted.org/Flask-Bootstrap/forms.html
- Flask WTF to generate forms in the backend quickly (especially using quickforms)
    * https://flask-wtf.readthedocs.io/en/stable/ 

## Testing (section TBC)

I am planning to perform manual and potentially also automated testing using PyTest (not yet included in the packages) :
https://flask.palletsprojects.com/en/1.0.x/testing/ 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

- Virtual Environment: 
    * a venv 'mongo-flask-venv' has been created locally to better control the module versions used and limit the requirement.txt file to the scope of our Flask app (instead of installing all our python modules..)

- Configuration files: 
    * Procfile has been coded to tell Heroku to execute the Flask app
    * requirements.txt based on the Virtual Environment have been stored on the Git Repo
    * .gitignore: the virtual Environment has been excluded from Git as it is already reflected in the requirements.txt

- Environment variables on Heroku: 
    * 'MONGOPWD': MongoDB's password for safety
    * the 'IP' address and 'PORT' of our flask app as suggested in Code Institute's tutorials


## Credits

### Content
- The items added to our Price Tracker app are all from Amazon

### Media
- No media used at this stage

### Acknowledgements

- I received inspiration for this project from 
    * Simo Edwin https://github.com/DevEdwin
    * Corey Schaefer Beautiful Soup courses https://coreyms.com/ 
    * Best practices for web scraping here: https://medium.com/python-pandemonium/6-things-to-develop-an-efficient-web-scraper-in-python-1dffa688793c 
