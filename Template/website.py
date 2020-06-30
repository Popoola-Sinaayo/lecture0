import os
from flask import Flask, request, render_template
from class1 import *
from class2 import *

app = Flask(__name__, template_folder='./templates')

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://postgres:Prayer1020@localhost:5432/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route('/')
def web1():



    return render_template("web1.html")

@app.route('/submit', methods=["POST"])
def web2():
    FirstName = request.form.get("FirstName")
    LastName = request.form.get("LastName")
    Email = request.form.get("Email")
    Gender = request.form.get("Gender")
    Commment = request.form.get("Commment")
    if FirstName == "" or LastName == '' or Email == '' or Gender == '' or Commment == '':
        return render_template("web1.html", message="Please fill out the required fields")
    Users = Website.query.all()
    for u in Users:
        u = u.Email
    if u == Email:
        return render_template("web1.html", meassage1 = "This email has already been used")
    User = Website(FirstName, LastName, Email, Gender, Commment)
    db.session.add(User)
    db.session.commit()


    return render_template("web2.html", FirstName=FirstName)

@app.route('/submit1', methods=["POST"])
def web3():
    UserName = request.form.get("UserName")
    Password = request.form.get("Password")
    User = Website2(UserName, Password)
    db.session.add(User)
    db.session.commit()
    return render_template("web3.html", UserName=UserName)

if __name__ == "__main__":
    web1()
