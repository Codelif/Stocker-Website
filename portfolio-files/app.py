#!portfolio-venv/bin/python3

from flask import Flask, render_template, url_for, request, redirect
import json

app = Flask(__name__)

from parseData import Nse

nse = Nse()
allQuotes = nse.all_codes()
storedScrip = []



@app.route("/")
def index():
    global allQuotes, storedScrip
    
    return render_template("test.html", stocks=storedScrip, quotes=allQuotes)

@app.route("/addScrip", methods=["POST", "GET"])
def addScrip():
    global storedScrip
    if request.method == "POST":
        user = request.form["addValue"]
        storedScrip.append(formatAddScrip(int(user)))
        return redirect(url_for("index"))

@app.route("/removeScrip", methods=["POST", "GET"])
def remScrip():
    global storedScrip
    if request.method == "POST":
        user = request.form["remValue"]
        print(user)
        storedScrip.pop(int(user))
        return redirect(url_for("index"))


def formatAddScrip(scrip):
    global allQuotes
    quotes = list(allQuotes)

    quote = quotes[scrip]
    quoteCompany = allQuotes[quote]

    intra = nse.get_intraday(quote)
    
    print(quote, quoteCompany)
    return {
        "company":quoteCompany,
        "quote":quote,
        "price":intra["Price"],
        "open":intra["Open"],
        "close":intra["Close"]
    }

    
