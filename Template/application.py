from flask import Flask, render_template, request

app = Flask(__name__, template_folder='./templates')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fall", methods=["POST"])
def fall():
    if request.method == "GET":
        return "Please submuit th form instaed"
    else:
        name = request.form.get("input1")
        return render_template("fall.html", name=name)

#def index():
#    now = datetime.datetime.now()
#    new_year = now.month == 1 and now.day == 1
#    new_year = True
#    return render_template("fall.html", new_year=new_year)


#@app.route("/")
#def index():
#    return render_template('index.html')

#def head():
#    name = "Thank you!"
#    return render_template("fall.html", name=name)
#@app.route("/bye")
#@app.route("/")
#def head():
#    name = "Thank you!"
#    return render_template("fall.html", name=name)
#@app.route("/bye")
#def foot():
#    name = "Goodbye"
#    return render_template("fall.html", name=name)
#def foot():
#    name = "Goodbye"
#    return render_template("fall.html", name=name)
