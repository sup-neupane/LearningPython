#API key is kind of like password which is requires to get data out of some API'S
#Like to withdraw money from bank you need to present your credentials
#Also API keys are used so that the provider knows we are not abusing their resources
import requests  #type: ignore
from dotenv import load_dotenv # type: ignore
import os


load_dotenv()  

api_key = os.getenv("API_KEY")


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["weather"][0]["main"])


