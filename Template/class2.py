import os
from flask_sqlalchemy import SQLAlchemy
from class1 import *

db = SQLAlchemy()

class Website2(db.Model):
    __tablename__ = "UserLogin"
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String)
    Password = db.Column(db.String)
    User_id = db.relationship("Website2", backref="Website", lazy=True)
    def __init__(self, UserName, Password):
        self.UserName = UserName
        self.Password = Password
