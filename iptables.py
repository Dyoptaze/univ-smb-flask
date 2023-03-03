# save this as app.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/start")
def start():
    return render_template("accueil.html")

@app.route("/rules_filter")
def rules_filter():
    return "rules_filter methode"

@app.route("/rules_nat")
def rules_nat():
    return render_template("reglesNAT.html")

@app.route("/rules_nat_add")
def rules_nat_add():
    return render_template("ajouterNAT.html")

@app.route("/alias")
def alias():
    return render_template("alias.html")
