from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/404")
def error():
    return render_template("404.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/watchlist")
def watchlist():
    return render_template("table.html")

app.run(debug=True, )