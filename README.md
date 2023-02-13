# backend-event-planner-in-spanish
## Table of Contents 
1. Description of the application
2. Technologies 
3. List of dependencies
4. Instructions for setting up the application




## Description of the application
The purpose of this application is to create a backend for the event planner in Spanish. 


This application uses SQL Alchemy and stores data on Heroku to create two tables. One holds information about people who are interested in scribing to the newsletter and the other table is to store information about events. Lastly uses routes to send and modify the information in the database. This application was deployed on Heroku. 


One table contains information regarding the people subscribing to the newsletter. This table  has a route to access the data stored and models to know which type of object is acceptable to the table. There are routes to post new information regarding the contact information of a person, get all the contact information in the database, and get a specific contact based on the id.  

The second table created is used to store the information regarding the events. This table has a model that establishes ways in which the data is accepted. This table has multiple routes such as posting an event, modifying the information of an event, getting all the events, and getting an event by date.  

There is also a file that checks if the event information id and the contact information id are valid. This can be useful when referencing an event or retrieving contact information.  

## Technologies

- PostgresSQL
- Postman
- Python

## List of dependencies (This should be found in the root file should be named requirements.txt)
- alembic
- attrs
- autopep8
- blinker
- certifi
- chardet
- click
- Flask
- Flask-Cors
- Flask-Migrate
- Flask-SQLAlchemy
- gunicorn
- idna
- iniconfig
- itsdangerous
- Jinja2
- Mako
- MarkupSafe
- packaging
- pluggy
- psycopg2-binary
- py
- pycodestyle
- pyparsing
- pytest
- pytest-cov
- python-dateutil
- python-dotenv
- python-editor
- requests
- six
- SQLAlchemy
- toml
- urllib3
- Werkzeug



