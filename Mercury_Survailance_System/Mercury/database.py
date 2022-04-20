from datetime import datetime
from Mercury import db, login
from flask_login import UserMixin
# code for login Dasabase models

@login.user_loader  # we use login_manger to allow users to login and logout
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin): #usermixin adds all the required methods needed for the login_manger
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(100),unique=True,nullable=False)
    image_file = db.Column(db.String(21),nullable=False, default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    
    def __repr__(self): # how are object is printed
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
