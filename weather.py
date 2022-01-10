import json
import pywttr
 
def weatherCheck():
    with open("config.json", "r") as jsonfile:
        config = json.load(jsonfile)

    city_name = config["city_name"]
    forecast = pywttr.en.get_forecast(city_name)

    #getting temperature
    temp = forecast.weather[0].avgtemp_f
    
    #getting weather description -- returns a list
    getDesc = forecast.current_condition[0].weather_desc

    #stripping the extra stuff around it to just get the description
    stripDesc = str(getDesc).replace("[WeatherDescItem(value='", "") 
    desc = stripDesc.replace("')]","")
    return (temp,desc)


    

if __name__ == "__main__":
    print("The temperature right now is: " + weatherCheck()[0] + " degrees Fahrenheit")
    print("The weather today is: " + weatherCheck()[1])

    

