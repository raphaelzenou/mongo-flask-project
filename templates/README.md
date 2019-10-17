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

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- Python 3.7.0
    * https://www.python.org/
- Flask 1.1.1 our Python web framework
    * https://palletsprojects.com/p/flask/ 
- Flask-PyMongo 2.3.0 to Interact with our MongoDB Atlas noSQL database
    * https://pypi.org/project/Flask-PyMongo/ 
- Beautifulsoup4  4.8.1 for Web Scraping
    * https://pypi.org/project/beautifulsoup4/ 
- Materialize CSS Framework 
    * https://materializecss.com/



## Testing (section TBC)

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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
