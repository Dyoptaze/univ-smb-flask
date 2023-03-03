# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/start")
def hello():
    return "Hello, World!"

@app.route("/rules_filter")
def hello():
    return "Hello, World!"

@app.route("/rules_nat")
def hello():
    return "Hello, World!"

@app.route("/rules_nat_add")
def hello():
    return "Hello, World!"

@app.route("/alias")
def hello():
    return "Hello, World!"
