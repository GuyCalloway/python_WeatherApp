from keys import darksky_key
# refactor to Environmental Variable
longitude = -79.3892455
latitude = 43.6425701
exclude = 'minutely, hourly, daily, alerts, flags'


def api_call(secret_key, latitude, longitude, exclude):
    url = f'https://api.darksky.net/forecast/{secret_key}/{latitude},{longitude}?exclude={exclude}'
    response = requests.get(url)
    dictionary = json.dumps(response.json(), sort_keys=True, indent=4)
    print(dictionary)
