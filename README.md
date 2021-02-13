# Django RBAC

A sample application to demonstrate RBAC

---
## Getting started 
These instructions will get you a copy of the project up and running in your local machine for development and testing purposes.

## Prerequisites
- [Git](https://git-scm.com/download/)
- [Python 3.9](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

## Installing
### Setting up pipenv
```pip3 install pipenv```
### Setting up the database
- Swith to postgres account (in terminal)
```sudo su - postgres```

- Run PostgreSQL command line client.
```psql```

- Create a database user with a password.
```CREATE USER 'name_of_user' with password 'db_password';```

- Create a database instance.
```CREATE DATABASE 'name_of_db' owner 'name_of_db' encoding 'utf-8';```

### Setting up and Activating a Virtual Environment
- Create a working space in your local machine
- Clone this [repository](https://github.com/KMaina/django_rbac/) `git clone https://github.com/KMaina/django_rbac.git`
- Navigate to the project directory
- Create a virtual environment `pipenv shell`
- Create a .env file and put these key=values in it:
```
export DB_NAME="your_db_name"
export DB_USER="your_postgres_username"
export DB_PASS="your_postgres_password"
export DB_HOST="localhost or any other host name"
export DB_PORT="port_number"
export SECRET_KEY="your secret"
```
- Load the environment variable `source .env`
- Sync dependencies to your virtual environment `pipenv sync`
- Migrate changes to the newly created database `python manage.py migrate`

## Starting the server
- Ensure you are in the project directory on the same level with `manage.py` and the virtual environment is activated
- Run the server `python manage.py runserver`

## Using the app
- In Postman navigate to `https://afternoon-ocean-11319.herokuapp.com/api/login/`
- Use the following credentials to log in
```
{
    "email": "att1@me.com",
    "password": "1234"
}
```
- Use the token to register new users into the app
## Run Tests
-Run your tests `pytest`

## API Spec
The documentation can be found on https://afternoon-ocean-11319.herokuapp.com/swagger/