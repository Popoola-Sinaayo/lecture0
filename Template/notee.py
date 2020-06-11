from flask import Flask, render_template, request
from flask_session import Session


app = Flask(__name__, template_folder='./templates')


app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
