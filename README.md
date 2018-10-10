# Python Flask REST Microservice 

REST API written in Python Flask using SQLAlchemy as the ORM with auto migration capabilities

## Pre-requisites
  - Download & install [Python 3.6](https://www.python.org/downloads/)
  - Download & install [Pipenv](https://docs.pipenv.org/)
   ```bash
    python -m pip install -U pip 
   ```
  - Download & Install [MySQL](https://www.mysql.com/) Server locally or use an external database (OPTIONAL)

## For Developers
  - Download & install [NodeJS](https://nodejs.org/en/download/) 
  - Install nodemon (use sudo if you in linux)
  ```bash
  npm i -g nodemon
  ```

## Installation

  ```bash
  # Clone the repository 
  git clone https://github.com/dipayan/python-flask-rest-microservice.git`
  # Change into the directory
  cd /python-flask-rest-microservice`
  # Install all required dependencies with
  pipenv install --system --deploy
  # Activate the project virtual environment
  pipenv shell
  # Create an local .env file and replace with the relevant values
  cp .env.sample .env
  ```
  You can also set the enviroment variables explicity (OPTIONAL)
  
  ```bash
  PORT=9000
  BUILD_DEV=development
  DATABASE_URL=postgres://name:password@host:port/dbname
  ```

## Running the application

  **Start the app**
  ```bash
  python run.py
  ```
  **Start the app for developers**
  ```bash
  nodemon run.py
  ```

## Database Auto migration & creation

You can create the tables using the following set of commands

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Author

Dipayan Biswas