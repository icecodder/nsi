from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Tout fonctionne parfaitement</p>"

app.run(debug=True)
