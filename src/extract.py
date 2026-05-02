import os
import requests
from dotenv import load_dotenv


load_dotenv()


def extract_weather_data():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = os.getenv("CITY")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Error al consultar API: {response.status_code} - {response.text}")

    data = response.json()

    return data