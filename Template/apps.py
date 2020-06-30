import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Users1(db.Model):
    __tablename__ = "UserDatabase1"
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String)
    LastName = db.Column(db.String)
    UserName = db.Column(db.String)
    Email = db.Column(db.String)
    Comment = db.Column(db.String)
    def __init__(self, FirstName, LastName, UserName, Email, Comment):
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.Email = Email
        self.Comment = Comment
