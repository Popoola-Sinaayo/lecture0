import os
import requests
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='./templates')
app.config["SECRET_KEY"] = "@&##**#*#*#$#"
socketio = SocketIO(app)
# defing an empty list
lst = []
# storing my votes in an api json object
votes = {"yes": 0, "no": 0, "maybe": 0}

@app.route('/')
def index():
    return render_template("index4.html", votes=votes)

# detects the submit vote function
@socketio.on("submit vote")
#defines a vote function passing in a data aurgument
def vote(data):
    #accessing the initial selection stored in the selection variable stored in a json notation in the Javascript code
    selection = data["selection"]
    # increasing the vote by 1 as the case may be
    votes[selection] += 1
    emit("vote totals", votes, broadcast=True)
socketio.run(app)
