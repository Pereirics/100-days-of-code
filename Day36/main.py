import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def send_messages(data, emoji, diff):
    account_sid = "AC072adbd938bfde88d0f44817786150a1"
    auth_token = os.environ.get("SMS_API_KEY")

    for article in data["articles"][0:3]:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK}: {emoji}{int(abs(diff))}%\nHeadline: {article['title']}\nBrief: {article['description']}",
            from_="+13203772770",
            to="+351932106455"
        )
        print(message.status)


def get_stock():
    parameters = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": STOCK,
        "interval": "60min",
        "apikey": os.environ.get("STOCK_API_KEY")
    }

    request = requests.get("https://www.alphavantage.co/query", params=parameters)
    request.raise_for_status()
    data = request.json()

    data = data["Time Series (60min)"]
    keys = list(data.keys())
    ys = float(data[keys[0]]["4. close"])
    bys = float(data[keys[16]]["4. close"])

    bys_date = keys[16][:10]

    diff = bys * 100 / ys - 100
    if abs(diff) >= 5:
        if diff > 0:
            emoji = "🔺"
        else:
            emoji = "🔻"
        get_news(bys_date, emoji, diff)


def get_news(bys_date, emoji, diff):
    parameters = {
        "qInTitle": COMPANY_NAME,
        "sortBy": "popularity",
        "from": bys_date,
        "pageSize": 3,
        "apiKey": os.environ.get("NEWS_API_KEY")
    }

    request = requests.get("https://newsapi.org/v2/everything", params=parameters)
    request.raise_for_status()
    data = request.json()

    send_messages(data, emoji, diff)


get_stock()
