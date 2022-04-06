from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

"""
These object will be used throughout project.
1.) Objects from this file can be included in many blueprints
2.) Isolating these object definitions avoids duplication and circular dependencies
"""

# Setup of key Flask object (app)
app = Flask(__name__)
dbURI = 'sqlite:///model/myDB.db'
# Setup SQLAlchemy object and properties for the database (db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
Migrate(app, db)
# Setup LoginManager object (app)
login_manager = LoginManager()
login_manager.init_app(app)

# __init__.py
from flask import Flask

# Setup of key Flask object (app)
app = Flask(__name__)

from flask_login import LoginManager

# The most important part of an application that uses Flask-Login is the LoginManager class.
# You should create one for your application like this:
# Setup LoginManager object (app)
login_manager = LoginManager()

# The login manager contains the code that lets your application and Flask-Login work together,
# such as how to load a user from an ID,  where to send users when they need to log in, and the like.
# Once the actual application object has been created, you can configure it for login with:

login_manager.init_app(app)