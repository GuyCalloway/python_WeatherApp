import requests
import json


def find_lat_and_lon(location, googlemaps_key):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?key={googlemaps_key}&address={location}'
    response = requests.get(url)
    dictionary = response.json()
    lat_lon = dictionary['results'][0]['geometry']['location']
    return lat_lon['lat'], lat_lon['lng']
