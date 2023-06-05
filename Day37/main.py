import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "pereirics"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": "pereirics",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph1_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2023, month=6, day=4)
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "21.8"
}

# response = requests.post(url=graph1_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "14.8"
}

# response = requests.put(url=pixel_endpoint, json=update_config, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_endpoint, headers=headers)
print(response.text)


