import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

with open("config.json") as config_file:
    config = json.load(config_file) 
    
app = Flask(__name__)
app.secret_key = config.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = config.get("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)

from app import routes