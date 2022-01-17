from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
#The secrets module provides functions for generating secure tokens
app.config['SECRET_KEY'] = '74d5fd2206e40898e7b7db95c190ef75'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../flask.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login first'
login_manager.login_message_category = 'info'

from resolution import routes