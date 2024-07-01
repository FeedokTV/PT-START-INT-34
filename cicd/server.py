from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>there could be a portal...or something else", 201

@app.route("/healthz")
def healthz():
    return "OK", 200