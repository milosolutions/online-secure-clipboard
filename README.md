js-encryption-app
=====
[<img src="https://static.milosolutions.com/static/img/logo-dark.png" height="40px"/>](https://milosolutions.com)

Overview
=====
js-encryption-app is an open source application based on Django and AngularJS that allows anyone to install a web application on their own server and share encrypted data using a password.


Installation
=====

1. Create a Python 2.7 virtualenv

2. Install dependencies:
	```
	pip install -r requirements.txt
	bower install
	```
3.  Create .env file:
	`mv env.example .env`
4. Create a database and put database URL to .env like this:
	`DJANGO_DATABASE_URL=postgresql://user:pass@ip/dbname`
5. Set up other environment variables such as **DJANGO_SECRET_KEY**, **DJANGO_ALLOWED_HOSTS**, **DJANGO_STATIC_ROOT**, etc
6. Set up **DJANGO_ADMINS** in the following format:
	`name:email@domain.com`
7. This app is using celery to run background tasks. You will need to set up **CELERY_BROKER_URL** ([read more](http://docs.celeryproject.org/en/latest/getting-started/brokers/))
8. Create tables:
	`python manage.py migrate`
9. Collect static files:
	`python manage.py collectstatic`

Starting the project
=====
Development:
	`python manage.py runserver`
Now you can access the application using [127.0.0.1:8000](127.0.0.1:8000)
	
For production use we would suggest using [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/).

Starting Celery
=====
Development
----------
For development run: 
	`celery -A proj worker -B`
	
**Note**: This is convenient if you’ll never run more than one worker node, but it’s not commonly used and for that reason isn’t recommended for production use
For more [click here](http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#starting-the-scheduler).

Production
-----------
This project contains '**supervisor**' folder which has all required files to run celery as a daemon using [supervisord](http://supervisord.org/)

There are two options:
1. In case you don't use supervisor at all you can simply run:
	`supervisord -c supervisor/supervisord.conf`
2. In case you have supervisor running you can simply copy **celeryd.conf** and **celery_beat.conf** to your `supervisor/conf.d/` directory and change **directory** and **path to project** accordingly.

License
=====
This project is licensed under the terms of the MIT license.

	


