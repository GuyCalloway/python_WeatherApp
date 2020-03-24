import requests
import json


def forecast(lat_lon, exclude, darksky_key):
    url = f'https://api.darksky.net/forecast/{darksky_key}/{lat_lon[0]},{lat_lon[1]}?exclude={exclude}'
    response = requests.get(url)
    dictionary = json.dumps(response.json(), sort_keys=True, indent=4)
    return dictionary
