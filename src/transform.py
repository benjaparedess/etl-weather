import pandas as pd


def transform_weather_data(data):
    transformed_data = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather_description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }

    df = pd.DataFrame([transformed_data])

    return df