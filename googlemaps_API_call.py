import requests
import json


def find_lat_and_lon(location, googlemaps_key):
    url = f'https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY'
    response = requests.get(url)
    dictionary = json.dumps(response.json(), sort_keys=True, indent=4)
    return dictionary
