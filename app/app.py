from flask import Flask
import yfinance as yf
import json

app = Flask(__name__)


@app.route("/<ticker>")
def hello_world(ticker='GOOGL'):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period='1mo')
    # print(data)
    _json = data.to_json(orient='index')
    # print(_json)
    # print(type(_json))
    string = json.loads(_json)
    # print(string)
    lst = []
    for i in string:
        print(string[i])
        date = i
        open = round(string[i]['Open'], 2)
        high = round(string[i]['High'], 2)
        low = round(string[i]['Low'], 2)
        close = round(string[i]['Close'], 2)
        lst.append([date, open, high, low, close])
    print(lst)

    return str(lst)
