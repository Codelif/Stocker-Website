from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


from parseData import Nse

nse = Nse()
allQuotes = nse.all_codes()
storedScrip = []


@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/searchQuote/")
def searchQuote():
    return render_template("searchQuote.html")

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
    global storedScrip, allQuotes

    return render_template("table.html", stocks=storedScrip, quotes=allQuotes)

@app.route("/watchlist/addScrip", methods=["POST", "GET"])
def addScrip():
    global storedScrip
    if request.method == "POST":
        user = request.form["addValue"]
        storedScrip.append(formatAddScrip(int(user)))
        return redirect(url_for("watchlist"))

@app.route("/watchlist/removeScrip", methods=["POST", "GET"])
def remScrip():
    global storedScrip
    if request.method == "POST":
        user = request.form["remValue"]
        print(user)
        storedScrip.pop(int(user))
        # storedScrip.append(formatAddScrip(int(user)))
        return redirect(url_for("watchlist"))


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


# app.run(debug=True, )