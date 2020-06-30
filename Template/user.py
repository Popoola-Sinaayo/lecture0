import os
from flask import Flask
from apps import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://postgres:Prayer1020@localhost:5432/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


def main():
    user = Users1("Popoola", "Sinaayo", "Popsin", "olusegunpopoola", "test")
    db.session.add(user)
    db.session.commit()
if __name__ == "__main__":
    with app.app_context():
        main()
