#defining a function that accesses the weather at my location

import requests, json

with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    # print("Read successful") 

#honestly relied heavily on a tutorial, but I think I understand how it works now

def weatherCheck():
    print("Here's the weather for today")
    # Inserting API key and location from config file
    api_key = data['key']
    city_name = data["city_name"]
    
    # fetch_url variable will fetch data from OWM API
    fetch_url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + api_key + "&q=" + city_name
    
    # request module has a get method, we use it to return our response
    response = requests.get(fetch_url)
    
    # response returns something in json, we convert it to python
    x = response.json()
    
    # If we don't get a 404 error (meaning we found the city)
    if x["cod"] != "404":

        # as far as I can tell, this is just fancy OWM API syntax giving me all the info I want, which is cool.
    
        # store the value of "main" key in variable y
        y = x["main"]
    
        # store the value corresponding to the "temp" and "humidity" key of y
        current_temperature_kelvin = y["temp"]
        
        # K -> F conversion
        current_temperature = round(((current_temperature_kelvin - 273.15) * (9/5) + 32),2)
        
        current_humidity = y["humidity"]

        # store the value of "weather" key in variable z
        z = x["weather"]
    
        # store the value corresponding to the "description" key at the 0th index of z
        weather_description = z[0]["description"]
    
        # print following values
        print("    Temperature (F): " +
                        str(current_temperature) +
            "\n    humidity: " +
                        str(current_humidity) + "%"
            "\n    description: " +
                        str(weather_description))
    
    else:
        print(" Sorry! My API doesn't have this city. Try again!")

