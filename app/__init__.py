from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Create the Flask app instance
app = Flask(__name__, template_folder='../templates')

# Configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI

# Initialize the database
db = SQLAlchemy(app)

# Import the views (this must be done after the app is created and configured)
from app import views
