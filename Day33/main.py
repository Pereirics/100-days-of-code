import requests
from datetime import datetime
import smtplib
from time import sleep

EMAIL = "happybirthdaybot4@gmail.com"
PASSWORD = "omhyrtykmqkyqdot"

LAT = 41.507948
LOG = -8.756225

def iss_is_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude - LAT) <= 5 and abs(iss_longitude - LOG) <= 5:
        return True

def is_night():
    parameters = {
        "lat": LAT,
        "log": LOG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset <= time_now or time_now <= sunrise:
        return True

while True:
    if iss_is_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="lifeofjoao@gmail.com",
            msg="Subject:ISS is visible!\n\nGo outside and look for the ISS!"
        )
    sleep(60)
