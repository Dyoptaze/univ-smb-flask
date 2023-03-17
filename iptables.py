# save this as app.py
from flask import Flask
from flask import render_template
from flask import json
from flask import request
from flask import session

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("connexion.html")


@app.route("/connexion",  methods=['POST'])
def connexion():
    if request.form['Login'] == "test" and request.form['Password'] == "pass":  
            #tester si mdp et login ok
        return render_template("accueil.html")
    else:
        msg = "La connexion a échoué, veuillez réessayer."
        return render_template("connexion.html", message = msg)


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


@app.route("/rules_nat_add", methods=['GET', 'POST'])
def rules_nat_add():
    if request.method == 'POST':
        if not request.form['ipsource'] == "" and not request.form['portsource'] == "" and not request.form['ipdest'] == "" and not request.form['portdest'] == "":
            with open("static/nat.json", "r+") as nat_file:
                file_data = json.load(nat_file)
                data = {'ipsource': request.form['ipsource'], 'portsource': request.form['portsource'], 'ipdest': request.form['ipdest'], 'portdest': request.form['portdest']}
                file_data.append(data)
                nat_file.seek(0)
                json.dump(file_data, nat_file, indent = 4)
            msg = "La règle NAT a été ajoutée."
        else: 
            msg = "La règle n'a pas été ajoutée, il faut saisir toutes les informations"
        return render_template("ajouterNAT.html", message=msg)
    else:
        return render_template("ajouterNAT.html")

@app.route("/alias")
def alias():
    with open("static/alias.json") as alias_file:
        data = json.load(alias_file)
    return render_template("alias.html", alias=data)
