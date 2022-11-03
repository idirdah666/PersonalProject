import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt").read().strip()
CITY = "Boulder"
UNITS = "imperial"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&units=" + UNITS

response = requests.get(url).json()
feels_like = response["main"]["feels_like"]
wind_speed = response["wind"]["speed"]
sunset_time = dt.datetime.fromtimestamp(response["sys"]["sunset"])
conditions = response["weather"][0]["description"]

print(f"The weather today is going to be {conditions}.")
if conditions == "snow":
    print("It's looking snowy today. Take the train!")

if conditions == "rain":
    print("It's looking rainy today. Bring a jacket with a hood!")


print(f"It feels like {feels_like} degrees in Boulder right now.")
print(f"The wind speed is {wind_speed} mph.")

if feels_like < 60 and wind_speed > 10:
    print("It's cold and windy. Wear a jacket.")

if feels_like > 70 and feels_like < 80 and wind_speed < 5:
    print("It's a perfect day today. Wear a t-shirt.")

sunset_time_standard = sunset_time.strftime("%I:%M %p")
print(f"The sunset time today is going to be {sunset_time_standard}.")






