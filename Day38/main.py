import requests #type:ignore
from datetime import datetime
from dotenv import load_dotenv # type: ignore
import os


load_dotenv()  

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")
BEARER = os.getenv("BEARER")

MY_WEIGHT = os.getenv("MY_WEIGHT")
MY_HEIGHT = os.getenv("MY_HEIGHT")
MY_AGE = os.getenv("MY_AGE")
GENDER = os.getenv("GENDER")




exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("sheet_endpoint")

exercise_text = input("Tell me which exercises you did: ")

parameters = { 
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg" : MY_WEIGHT,
    "height_cm" : MY_HEIGHT,
    "age" : MY_AGE,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


response = requests.post(exercise_endpoint, json=parameters , headers= headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheets_headers = {
    "Authorization": f"Bearer {BEARER}",
}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers= sheets_headers)

print(sheet_response.text)




