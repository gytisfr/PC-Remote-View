import flask, mss
from flask import Flask, request
from mss import mss

app = Flask(__name__, static_folder='templates')

@app.route("/")
def index():
    screenshot = mss().shot(mon=1, output="templates/screenshot.png")
    return flask.render_template("index.html")

app.run("192.168.1.78", port=3, debug=True)