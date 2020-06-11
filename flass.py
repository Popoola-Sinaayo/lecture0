from flask import Flask

app = Flask(__name__)

@app.route("/")
def indent():
    return "HEllo world"


@app.route("/<string:name>")
def index(name):
    name = name.capitalize()
    return f"hello, {name}!"
