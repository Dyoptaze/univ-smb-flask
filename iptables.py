# save this as app.py
from flask import Flask
from flask import render_template
import json

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
    with open("static/nat.json") as nat_file:
        data = json.load(nat_file)
    return render_template("reglesNAT.html", nat=data)

@app.route("/rules_nat_add")
def rules_nat_add():
    return render_template("ajouterNAT.html")

@app.route("/alias")
def alias():
    with open("static/alias.json") as alias_file:
        data = json.load(alias_file)
    return render_template("alias.html", alias=data)
