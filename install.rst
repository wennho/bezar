----------------
Installation steps
----------------

- Install MySQL 
	- ``sudo apt-get mysql-server``
	- Create a database called *bezar*, with a blank password.

- Install Django ``pip install django``
    
- Install Scrapy ``pip install scrapy``

- In *bezar/bezar/settings.py*, add the installation location to TEMPLATE_DIRS and STATICFILES_DIRS 

----------------
To Run
----------------

- Start the MySQL server

- In the bezar root directory, run ``python manage.py syncdb``. This creates the tables in the database

- Start the server with ``python manage.py runserver``. You can now view the website in `localhost:8000/ads`
