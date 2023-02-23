import requests
import json

api_key = "Your API Key Here from Openweathermap"
city = input("Which city would you like: ")
units = input("Metric of Imperial measurements: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"

response = requests.get(url)
data = json.loads(response.text)

if response.status_code == 200 and data["cod"] == 200:
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    print(f"The temperature in {city} is a low of {temp_min} degrees and a high of {temp_max} degrees")
    print(f"The humidity in {city} is {humidity}%.")
    print(f"The wind speed in {city} is {wind_speed} meters per second.")
else:
    print("Invalid City Name or Measurement Type")