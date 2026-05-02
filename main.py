from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.load import load_weather_data


raw_data = extract_weather_data()
clean_data = transform_weather_data(raw_data)
load_weather_data(clean_data)

print("Pipeline ejecutado correctamente")