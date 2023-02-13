
## Instructions for setting up the application

## Table of Contents 
1. Managing Dependencies
2. Setting the Databases
3. Creating a '.env' File
4. Run '$flask db init'
5. Run '$flask run'
  
 
 ### Managing dependencies (Install dependencies at the root of your project where requirements.txt is available or this may cause issues in the future).

1. Create a virtual environment 

```bash
$ python3 -m venv venv
```

2. Activate the environment (This step is used when activating your environment) 

```bash
$ source venv/bin/activate 
```

3. Install the dependencies 

```bash
$ pip install -r requirements.txt
```

### Setting the Databases (once connected the computer should have “postgres=#” next to the input.

1. Download postgres
2. Open postgres in your terminal 

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

