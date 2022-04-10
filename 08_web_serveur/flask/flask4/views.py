from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    date = datetime.now()
    h = date.hour
    m = date.minute
    s = date.second
    return render_template("index.html", heure=h, minute=m, seconde=s)

app.run(debug=True)
