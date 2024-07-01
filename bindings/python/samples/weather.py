
import requests
import requests

lat=38.6631
lon=-90.5771
weatherinfo=""
def get_weather(lat=38.6631, lon=-90.5771):
    weatherinfo = "Weather Info:   "

    # Call the first API to get the forecast URL
    response = requests.get("https://api.weather.gov/points/" + str(lat) + "," + str(lon))
    data = response.json()
    forecast_url = data["properties"]["forecast"]

    # Call the forecast URL API to get the forecast data
    response = requests.get(forecast_url)
    data = response.json()
    forecast = data["properties"]["periods"]

    # Print the first 5 elements of the forecast array
    for i in range(5):
        weatherinfo += " *** " + forecast[i]["name"] + ": " + forecast[i]["detailedForecast"]

    return weatherinfo

#weatherinfo = get_weather(lat, lon)
#print(weatherinfo)

