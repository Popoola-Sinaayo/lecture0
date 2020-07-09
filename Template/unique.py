import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def index2():
    return render_template('index2.html')


@app.route('/convert', methods=["POST"])
def convert():
    currency = request.form.get("currency")
    res = requests.get("http://data.fixer.io/api/latest?access_key=3bd73b0f7d8feaa4600ddacbc7b8643a&format=1", params={
    "base": "EUR", "symbol": currency
    })
    if res.status_code != 200:
        return jsonify({"success": "False"})


    data = res.json()
    if currency not in data["rates"]:
        return jsonify({"success": "False"})

    return jsonify({"success": True, "rate": data["rates"][currency]})
