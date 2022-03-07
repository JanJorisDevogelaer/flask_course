from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create an instance of class Flask
webapp = Flask(__name__)  # __name__ = Python predefined variable
webapp.config.from_object(Config)

# Create the database
db = SQLAlchemy(webapp)
migrate = Migrate(webapp, db)


# has to be on the bottom as workaround for circular imports
# routes.py contains the structure of the webapp
from app import routes, models


# # Debugging
# from app.models import User
# u = User(username="Jan", email="jjd@mail.com")
# print(u)