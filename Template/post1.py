import time
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def index():
    return render_template('post2.html')

@app.route('/posts', methods=["POST"])
def posts():
    # gets the start and the end point for post to generate
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or start + 9)

    # bgenerate list of posts
    data = []

    for i in range(start, end+1):
        data.append(f"Post #{i}")


    time.sleep(1)
    # returns json list of posts

    return jsonify(data)
