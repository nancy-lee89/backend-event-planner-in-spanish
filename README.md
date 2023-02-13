# backend-event-planner-in-spanish
## Table of Contents 
1. Description of the application
2. Technologies 
3. List of dependencies
4. Instructions for setting up the application
	- Managing Dependencies
	- Setting the Databases
	- Creating a '.env' File
	- Run '$flask db init'
	- Run '$flask run'



## description of the application
The purpose of this application is to create a backend for the event planner in Spanish. 


This application uses SQL Alchemy and stores data on Heroku to create two tables. One holds information about people who are interested in scribing to the newsletter and the other table is to store information about events. Lastly uses routes to send and modify the information in the database. This application was deployed on Heroku. 


One table contains information regarding the people subscribing to the newsletter. This table  has a route to access the data stored and models to know which type of object is acceptable to the table. There are routes to post new information regarding the contact information of a person, get all the contact information in the database, and get a specific contact based on the id.  

The second table created is used to store the information regarding the events. This table has a model that establishes ways in which the data is accepted. This table has multiple routes such as posting an event, modifying the information of an event, getting all the events, and getting an event by date.  

There is also a file that checks if the event information id and the contact information id are valid. This can be useful when referencing an event or retrieving contact information.  

## Technologies

- PostgresSQL
- Postman
- Python

## list of dependencies (This should be found in the root file should be named requirements.txt)
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


## Instructions for setting up the application
### Managing dependencies (Install dependencies at the root of your project where requirements.txt is available or this may cause issues in the future).

Create a virtual environment 
```bash
$ python3 -m venv venv
```

Activate the environment (This step is used when activating your environment) 
```bash
$ source venv/bin/activate 
```
Install the dependencies 
```bash
$ pip install -r requirements.txt
```
### Setting the Databases (once connected the computer should have “postgres=#” next to the input.
Download postgres
Open postgres in your terminal 
```bash
$ psql -U postgres
```
Create a database
```bash
$ CREATE DATABASE name_of_database;
```
Check database was created 
```bash
$ \l
```
Connect to the database 
```bash
$ \c  name_of_database
```
Check that you have no tables inside your database or this can cause complications in your project (might need to drop database) 
```bash
$ \dt
```
## Creating a `.env` File
Create a file named `.env`.

Create one environment variables that will hold your database URLs.

`SQLALCHEMY_DATABASE_URI` to hold the path to your development database


Your `.env` may look like this:

```
FLASK_ENV=production
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/task_list_api_development
```

## Run `$ flask db init`

Next to create the tables on your computer do the following. 
** If working with multiple people only run this on only one computer 
```bash
$ flask db init
```
Next run the following command 
```bash
$ flask db migrate
$ flask db upgrade
```
Then in your terminal you can check your data tables, by running the following commands. 
```bash
$ psql -U postgres
$ \l
$ \c  name_of_database
$ \dt
```

## Run `$ flask run`

Then you can check, modify your database while running `$ flask run` in your terminal.
