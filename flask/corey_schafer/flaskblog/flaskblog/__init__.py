from flask import Flask
from flaskblog import config, mail_credentials
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flaskblog.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

bcrypt = Bcrypt()

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
