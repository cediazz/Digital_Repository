# Digital_Repository
This is a very simple repository website built with Django.

# Project Summary
The website displays all types of documents in PDF format. Documents can be uploaded, downloaded and viewed in detail. The user can authenticate in the system to upload their own documents or delete them

## Running this project
To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can create virtual environment with
````markdown
python -m venv virtual_environment_name(Windows)
virtualenv .(Linux)
````
Open the virtual environment folder and clone or download this repository with
````markdown
git clone https://github.com/cediazz/Digital_Repository.git
````
Activate the virtual environment and install the project dependencies with
````markdown
pip install -r requirements.txt
````
Create the .env file and place the environment variables you need
````markdown
SECRET_KEY='your secret key'
ENGINE='your database engine'
DB_NAME=your database name
DB_USER=your database user
DB_PASSWORD=your database password
DB_HOST=your database host
DB_PORT=your database port
````
Now you can run the project with this command
````markdown
python manage.py runserver
````
