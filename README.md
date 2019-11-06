# Price Tracker for Amazon with value storage

Price Tracker is an app where users can add amazon links and store the price and characteristics of the items they like in a noSQL MongoDB Atlas database.

The idea is to combine Python's Beautiful Soup web scrapper with the Flask mini framework and Mongo DB (using PyMongo) in the Back End and a standard CSS framework in the Front End.

Hosting will be powered by Heroku connected with GitHub (not Heroku Git) for deployments.

## UX

Users will be able to add an amazon link via a form and then add the concerned item to their tracked products.
Users will also be able to edit, delete entries to offer them the full CRUD experience.

Users will have access to all their 'Amazon Portfolio' entries but also other users' and will be able to see and edit product characteristics.

Optional features to potentially be added to make the UX even better:
- Including Amazon sections not in scope as: Kindle, Books in general and basically any other media (audio, video) that can be both physical and digital.
- A user login system is not required for the project, but it can easily be added in the future as user management is already well defined and used throughout the app.
- An email alert system using Gmail's SMTP if we also add a price tracking system.

## Features
 
### Existing Features

- Create : Users will be able to add an amazon link via a form and then add the concerned item to their tracked products.
- Read : Users will have access to all their entries and will be able to see wether the current price is the lowest since they started tracking a product so as to help them make a decision on whether now is a good time to buy it.
- Update / Delete : Users will also be able to edit, delete entries to offer them the full CRUD experience.

### Features Left to Implement
- Login system:  a user login system is not required for the project, but I am thinking of adding one if time permits).
- Email alerts: an email alert system using Gmail's SMTP.
- CRON : runs on UNIX (equivalent to Django CRON) enabling us to store and track historical prices so users can have a look at the trends and / or be alerted in case of favourable price changes.
https://pythonprogramming.net/crontab-tutorial-basics/

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- Python 3.7.0 > the base Backend Language
    * https://www.python.org/
- Flask 1.1.1 > Web framework
    * https://palletsprojects.com/p/flask/ 
- Flask-PyMongo 2.3.0 > MongoDB database package
    * https://pypi.org/project/Flask-PyMongo/ 
- Requests 2.22.0 > HTTP requests
    * Used to get information from websites using HTTP requests
    * https://requests.kennethreitz.org/en/master/
- Beautifulsoup4  4.8.1 > for Web Scraping
    * Used to parse website code obtained using the Requests library
    * https://pypi.org/project/beautifulsoup4/ 
- Materialize or Bootstrap CSS Framework > Front End
    * https://materializecss.com/
    * https://getbootstrap.com/
- Dot-Env > Simplified Environment Variables Management
    * https://simpleit.rocks/python/flask/managing-environment-configuration-variables-in-flask-with-dotenv/
    * https://pypi.org/project/python-dotenv/
- Flash Messages > Informing users of CRUD operations
    * https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/#message-flashing-pattern 
- UnitTest > Testing
    * https://docs.python.org/3/library/unittest.html
    * https://github.com/realpython/discover-flask

Technologies considered but not used :
- Flask Bootstrap for an easier Bootstrap integration notably with the WTF package
    * https://pythonhosted.org/Flask-Bootstrap/forms.html
- Flask WTF to generate forms in the backend quickly (especially using quickforms)
    * https://flask-wtf.readthedocs.io/en/stable/ 
- ReCaptcha > to avoid abuse and automation on forms
    * https://techmonger.github.io/5/python-flask-recaptcha/ 
- Selenium > to go further in preventing Amazon from blocking scraping
    * https://selenium-python.readthedocs.io/

## Testing and Error Management

Amazon has implemented anti web scraping systems so we referred to a guide of the best practices for web scraping (see Acknowledgements) and :
- on one hand made sure to trim the URL to the minimum viable urls to limit tracking from Amazon with extra url parameters and - on the other hand built an error.html page guiding users in case of blocking.

Further information on amazon scraping issues can be found here :
https://stackoverflow.com/questions/41366099/getting-blocked-when-scraping-amazon-even-with-headers-proxies-delay

The aforementioned error page is also useful when users have pasted either:
- links where no specific price is selected
- links that are from Amazon sections not in scope as: Kindle, Books in general and basically any other media (audio, video) that can be both physical and digital.


I have performed to perform manual and developed some automated tests using the UnitTest package.

- Error Handling : 
    * The new_item_conf_func has an inbuilt error handling system linked to error.html that can take care of any possible errors (even those that I might not have detected yet)
    * Some error messages have been made explicit for the users e.g. the URL not being an Amazon one
    * A small Troubleshooting section appears in error.html to guide users in case of error
    * The user can go back to the form without entering the username again for a better UX

- Manual Tests:

    * Countries : tried running the app with different pages from different countries' dedicatd websistes (e.g. amazon.com, amazon.de, amazon.it, amazon.es, amazon.fr...)
    * Wrong URLs : tried entering simple strings or what seemed to be urls (http or https .com type of structures)
    * Tried all possible combinations of the CRUD range


Automated Tests: see test.py

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
    * 'MONGODBNAME' : collection name for extra safety
    * 'MONGOLOGIN' :  admin login for extra safety too
    * 'IP' address and 'PORT' of our flask app as suggested in Code Institute's tutorials
    * 'SECRET_KEY' : for sessions (flash messages especially here)


## Credits

### Content
- The items added to our Price Tracker app are all from Amazon's website
- Note that we are not using the API here but rather scrape product pages

### Media
- Images are all coming from Amazon's product pages

### Acknowledgements
- I received great advice from my mentor Brian Macharia notably on how to structure the project and prioritise the different features and technologies. 
Brian also taught me the important writing slightly more elegant code (PEP8 concepts) even if I know there is still a long way to go for me.

- I received inspiration for this project from the following internet heroes :
    
    * Corey Schaefer for his Beautiful Soup courses https://coreyms.com/
    * Real Python for Tests https://github.com/realpython 
    * Simo Edwin for Amazon Scraping https://github.com/DevEdwin
    * Best practices for web scraping here: 
    https://medium.com/python-pandemonium/6-things-to-develop-an-efficient-web-scraper-in-python-1dffa688793c 
