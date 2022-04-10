"""
Max et Bastien
31/03/2022
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resultat", methods=["POST"])
def resultat():
    result = request.form
    nom = result["nom"]
    nombre_1 = int(result["nombre_1"])
    nombre_2 = int(result["nombre_2"])
    somme = nombre_1 + nombre_2
    return render_template("resultat.html", nom=nom, somme=somme)

app.run(debug=True)
