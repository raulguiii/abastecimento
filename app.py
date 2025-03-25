from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def do_login():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
