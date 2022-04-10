from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Tout fonctionne parfaitement</p>"

@app.route("/about")
def about():
    return "<p>Une autre page</p>"

app.run(debug=True)
