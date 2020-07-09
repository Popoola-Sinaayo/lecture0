import os
import eventlet
import gevent
import requests
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='./templates')

app.config["SECRET_KEY"] = "@&$*$($()@$($@))"
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index3.html")
# socketoi.on runs when it detects the submit vote function
@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    emit("announce vote", {"selection": selection}, broadcast=True)
socketio.run(app)
