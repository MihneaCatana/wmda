### **Exercise 1: Extracting and Cleaning Data from an API**
import requests
import pandas as pd

cities = [ "New York","London", "Tokyo", "Paris", "Berlin"]

weather_data = pd.DataFrame()

for city in cities:
    url = "https://wttr.in/"+city+"?format=%C+%t"
    response = requests.get(url)
    weather_info = response.text.strip().split(' ');

    weather_condition = weather_info[0]
    temperature = " ".join(weather_info[1:])

    if (temperature[0] == '+') or  (temperature[0] == '-') or (temperature[0] == '0'):
        temperature = temperature
    else:
        temperature = temperature.split(' ')[1]

    data = {
        "City": city,
        "Weather Condition": [weather_condition][0],
        "Temperature": [temperature]
    }

    city_data = pd.DataFrame(data)

    weather_data = pd.concat([weather_data, city_data], ignore_index=True)

weather_data.to_csv("weather_data.csv", index=False)


