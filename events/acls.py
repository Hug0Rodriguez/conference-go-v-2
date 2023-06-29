from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import json
import requests


def get_photo(city, state):
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_API_KEY}
    query = {"query": f"{city} , {state}"}

    response = requests.get(url, params=query, headers=headers)
    content = json.loads(response.content)

    try:
        picture_url = content["photos"][0]["src"]["original"]
        return {"picture_url": picture_url}
    except (KeyError, IndexError):
        return {"picture_url": None}


def get_weather(city, state):
    # get the latitude and longitude of the city and state
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {"q": f"{city}, {state}", "appid": OPEN_WEATHER_API_KEY}
    response = requests.get(url, params=params)
    content = response.json()
    lat = content[0]["lat"]
    lon = content[0]["lon"]
    # use the latitude and longitude to get the weather
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "units": "imperial",
        "appid": OPEN_WEATHER_API_KEY,
    }
    response = requests.get(url, params=params)
    content = response.json()
    description = content["weather"][0]["description"]
    temp = content["main"]["temp"]
    return {"description": description, "temp": temp}
