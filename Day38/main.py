import requests
import os
from datetime import datetime

GENDER = "male"
HEIGHT_CM = 172
WEIGHT_KG = 80
AGE = 20

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/07465208e877869e04a8efa285ddf1b7/myWorkouts/folha1"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

query = input("Tell me which exercises you made: ")

parameters = {
    "query": query,
    "gender": GENDER,
    "height_cm": HEIGHT_CM,
    "weight_kg": WEIGHT_KG,
    "age": AGE
}

request = requests.post(url=nutrition_endpoint, headers=headers, json=parameters)
request.raise_for_status()
result = request.json()

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    name_exercise = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    payload = {
        "folha1": {
            "date": today,
            "time": time,
            "exercise": name_exercise,
            "duration": duration,
            "calories": calories
        }
    }

    request = requests.post(url=sheety_endpoint, json=payload, headers=headers)
    request.raise_for_status()
    print(request.text)
