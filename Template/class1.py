import os
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Website(db.Model):
    __tablename__ = "WebsiteUser"
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String)
    LastName = db.Column(db.String)
    Email = db.Column(db.String)
    Gender = db.Column(db.String)
    Commment = db.Column(db.String)

    def __init__(self, FirstName, LastName, Email, Gender, Commment):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Gender = Gender
        self.Commment = Commment
