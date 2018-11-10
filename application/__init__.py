from flask import Flask
app = Flask(__name__)

# Get SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Configure SQLAchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views
from application.movies import models
from application.movies import views

# Create all needed tables
db.create_all()