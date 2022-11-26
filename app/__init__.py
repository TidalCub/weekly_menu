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

from app import routes