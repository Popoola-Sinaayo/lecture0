import os
from class1 import *
from class2 import *
from flask import Flask
# difning the name of the flask app
app = Flask(__name__)
#configuring the ult of the database to make flask communniacte with my application
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://postgres:Prayer1020@localhost:5432/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
