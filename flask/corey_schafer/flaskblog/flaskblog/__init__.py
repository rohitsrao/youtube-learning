from flask import Flask
from flaskblog import config
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt()

from flaskblog import routes
