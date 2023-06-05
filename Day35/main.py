import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
LAT = 40.507948
LOG = -8.756225
account_sid = "AC072adbd938bfde88d0f44817786150a1"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": LAT,
    "lon": LOG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

request = requests.get(OWM_ENDPOINT, params=parameters)
request.raise_for_status()
data = request.json()
weather_slice = data["hourly"][:12]

for hour in weather_slice:
    weather_id = hour["weather"][0]["id"]
    if int(weather_id) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to be raining today. Remember to brin an ☔.",
            from_="+13203772770",
            to="+351932106455"
        )
        print(message.status)
        break


