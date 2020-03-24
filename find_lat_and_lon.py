import requests
from keys import map_api_key


def find_lat_and_lon(location, map_api_key):
    url = f'https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY'
    response = requests.get(url)
    dictionary = json.dumps(response.json(), sort_keys=True, indent=4)
    print(dictionary)
