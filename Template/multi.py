from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template("index1.html")
    text = ["bnbnmdspbndpbmdbdbdbdbkdgbddbibonbonbdbdbdbdbdbdb",
    "dbdbdbdbdbdbdbdbddbdbdbdbdbdbdbdbdbdbdbdbdbddbdbdbbdbdbdbdbdbdbkhikrnogndgonighdpobjhdpgu0gbmddgig9hgdjhgpdhd0giue0ghjdhg09d8hgdh",
    "dghdhnpjhbjh-jh  ey]drghtg9hdghdg]g9hehgehbetgn9g09tohmrhtjeihnedghdeghfnpjmrjhedgnrgbhojrhgjfpbn-eihnedghdeghfnpjmrjhrhgju0deuhr"]

@app.route('/first')
def first('/'):
    return text[0]
@app.route('/second')
def second():
    return text[1]


@app.route('/third')
def third():
    return text[2]
