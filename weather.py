import pywttr
import json

with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile)

city_name = config["city_name"]

def weatherCheck():
    forecast = pywttr.en.get_forecast(city_name)
    return(forecast.weather[0].avgtemp_f),
