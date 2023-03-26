from flask import Flask
from config import Config
# Import for Flask Db and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import for Flask Login
from flask_login import LoginManager

# Create flask app variable
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login Config
login = LoginManager(app)
login.login_view = 'login' # Specify what page to load for NON-authenticated Users

login.login_message_category = 'danger'

from app import routes,models