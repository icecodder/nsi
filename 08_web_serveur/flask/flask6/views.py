from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resultat", methods=["GET"])
def resultat():
    result = request.args
    n = result["nom"]
    p = result["prenom"]
    return render_template("resultat.html", nom=n, prenom=p)

app.run(debug=True)
