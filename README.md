# opply_task
Backend for Opplymob Technical Task

Backend Logic for Ecommerce application based on requirements on https://gist.github.com/martinOpply/c0b496ae1c52ec24899b58bea6b4708d

SETUP:

Setup virtual environment
```
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

Setup a postgresql database with name 'opplymob' and a user 'opply'.
Configure the settings.py file with the credentials and port number once the database is up and running.


USAGE: 
Once DB is setup, run the following commands to start a development server:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Once the server is running, you can import the postman collection and use the Register User API to get token for a user with username and password in the form data.

Copy the access token and pass as Bearer token in header for the remaining apis.

TESTS:

#TODO
Ref : https://coverage.readthedocs.io/en/6.5.0/install.html

DEPLOYMENT FOR AWS:

setup an ec2 instance and then connect to it via ssh. Database can be on RDS postgres.

Then run the following commands
```
sudo apt-get install python3-pip
sudo pip3 install gunicorn
sudo apt-get install supervisor
sudo apt-get install nginx
sudo pip3 install django
```
