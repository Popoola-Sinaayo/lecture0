import os
from flask import Flask, request, render_template
from class1 import *
from class2 import *

app = Flask(__name__, template_folder='./templates')

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://postgres:Prayer1020@localhost:5432/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route('/')
def web0():
    return render_template("web0.html")

@app.route('/signup')
def web():
    return render_template("web1.html")

@app.route('/submit', methods=["POST", "GET"])
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
    Users = Website2.query.all()
    for user in Users:
        use = user.UserName
    if UserName == use:
        return render_template("web2.html", message="This Username has already been Used Please try Another Username", UserName=UserName)
    else:
        User = Website2(UserName, Password)
        db.session.add(User)
        db.session.commit()
        return render_template("web3.html", UserName=UserName)
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("web0.html")
    else:
        UserName = request.form.get("UserName")
        Password = request.form.get("Password")
        User = Website2.query.all()
        for Use in User:
            UserNames = Use.UserName
        for Us in User:
            UserPassword = Us.Password
        if UserName == '' or Password == '':
            return render_template("web0.html", message="Plesae Fill the required fields")
        if UserName == UserNames and Password == UserPassword:
            return render_template("web3.html", UserName=UserName, login="login Succesful")
        else:
            return render_template("web0.html", message="Invalid Credentials")

if __name__ == "__main__":
    web1()
