from pprint import pprint
from datetime import date, datetime
from pandas import read_csv, Series
from requests import Session
from json import dumps
from math import floor




def conv_ctime(date=(2020, 1, 1)):
    return str(floor(datetime(date[0], date[1], date[2], 5, 30).timestamp()))

class Nse():  
    def __init__(self):
        pass

    def all_codes(self, give_json=False):
        equity_csv = 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'
        df = read_csv(equity_csv)
        if give_json:
            return dumps(Series(df["NAME OF COMPANY"].values,index=df.SYMBOL).to_dict())
        return (Series(df["NAME OF COMPANY"].values,index=df.SYMBOL).to_dict())

    def get_intraday(self, code="", give_json=False):
        urlAPI = 'https://www.nseindia.com/api/quote-equity?symbol={}'.format(code.upper())
        urlFetchCookies = 'https://www.nseindia.com/get-quotes/equity?symbol={}'.format(code.upper())
        s = Session()
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',}
        s.get(urlFetchCookies, headers=headers)
        r = s.get(urlAPI, headers=headers).json()
        
        datetoday = date.today()
        currprice = r["priceInfo"]["lastPrice"]
        openprice = r["priceInfo"]["open"]
        closeprice = r["priceInfo"]["close"] if int(r["priceInfo"]["close"]) > 0 else "-"
        change = r["priceInfo"]["change"]
        
        ret = {"Date": str(datetoday.year)+"-"+str(datetoday.month)+"-"+str(datetoday.day), "Price":currprice, "Open":openprice, "Change":change, "Close":closeprice}
        
        if give_json:
            return dumps(ret)
        return ret
    
    def historical_data(self, code="", date_from=(2020, 1, 1), date_to=(2021, 1, 1), give_json=False):

        url = 'https://query1.finance.yahoo.com/v7/finance/download/{}.NS?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true'.format(code.upper(), conv_ctime(date_from), conv_ctime(date_to))
        
        df = read_csv(url).to_dict("list")
        # df.reverse()
        df.pop("Adj Close")

        dl = [list(i) for i in list(zip(df["Open"], df["High"], df["Low"], df["Close"]))]
        dd = list(df["Date"])
        a = []
        for i, j in list(zip(dd, dl)):
            if ('nan' in [str(h) for h in j]):
                continue
            c = i.split("-")
            dateiso = date(int(c[0]), int(c[1]), int(c[2]))
            b = {"x": dateiso.strftime("%d %b, %Y")}
            b.update({"y": j})
            a.append(b)
        
        # pprint(a)
        if give_json:
            return dumps(a)
        return (a)
    
    def live_quote(self, code=""):
        urlAPI = 'https://www.nseindia.com/api/quote-equity?symbol={}'.format(code.upper())
        urlFetchCookies = 'https://www.nseindia.com/get-quotes/equity?symbol={}'.format(code.upper())
        s = Session()
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',}
        s.get(urlFetchCookies, headers=headers)
        r = s.get(urlAPI, headers=headers).json()
        
        return r["priceInfo"]["lastPrice"]



