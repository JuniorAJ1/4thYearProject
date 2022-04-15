from flask import Flask
from flask_login import LoginManager, UserMixin, login_user
from flask_sqlalchemy import SQLAlchemy #used for the database
from flask_bcrypt import Bcrypt
from datetime import datetime

app=Flask(__name__)
app.config['SECRET_KEY']= '8ee2dbaad60f93b61022e297b9f840e5' #secret key which is used for protectection againt modifying cookies, and forgery attacks
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login = LoginManager(app)

from Mercury import Main