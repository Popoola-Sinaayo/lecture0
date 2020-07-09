from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")

text = ["bnbnmdspbndpbmdbdbdbdbkdgbddbibonbonbdbdbdbdbdbdb",
"dbdbdbdbdbdbdbdbddbdbdbdbdbdbdbdbdbdbdbdbdbddbdbdbbdbdbdbdbdbdbkhikrnogndgonighdpobjhdpgu0gbmddgig9hgdjhgpdhd0giue0ghjdhg09d8hgdh",
"dghdhnpjhbjh-jh  eydrghtg9hdghdg]g9hehgehbetgn9g09tohmrhtjeihnedghdeghfnpjmrjhedgnrgbhojrhgjfpbn-eihnedghdeghfnpjmrjhrhgju0deuhr"]


@app.route('/')
def index():
    return render_template("index1.html")


@app.route('/first')
def first():
    # returns the fisrt index of thge text defined above
    return text[0]
@app.route('/second')
def second():
    return text[1]


@app.route('/third')
def third():
    return text[2]
