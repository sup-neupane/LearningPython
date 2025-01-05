#HTTP Requests:
# GET     requests.get()
# POST    requests.post()
# PUT     requests.put()
# DELETE  requests.delete()
import requests #type: ignore
import datetime as dt

from dotenv import load_dotenv # type: ignore
import os


load_dotenv()  


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url = PIXELA_ENDPOINT, json = parameters)
# print(response.text)


graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "CyclingGraph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response.text)

paint_graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.datetime.now()


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you ride today?"),
}

response = requests.post(url=paint_graph_endpoint, json=pixel_data, headers=headers)
print(response.text)



update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
