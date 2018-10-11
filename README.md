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
  cd python-flask-rest-microservice`
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
## Usage

**API Specifications**
  - GET: /api/v1/todos/
  - GET: /api/v1/todos/?title= 
  - GET: /api/v1/todos/{todo_id}
  - POST: /api/v1/todos/
  - PUT: /api/v1/todos/{todo_id}
  - DELETE: /api/v1/todos/{todo_id}

**Example**
Get all todos
curl http://localhost:{PORT}/api/v1/todos

## Running the application as a Docker container

 ```bash
 cd python-flask-rest-microservice
 # Build the docker image 
 docker build -t python-flask-app .
 # Run the docker container and put the port as specified in the .env file
 docker run -d -p 9000:9000 --name python-flask-app -e PORT=9000 -e BUILD_ENV='development' -e DATABASE_URL='mysql+pymysql://user:pass@host:port/dbname' python-flask-app
 # Check the logs
 docker logs -f python-flask-app
 # Cleaup the container
 docker stop python-flask-app && docker rm python-flask-app
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