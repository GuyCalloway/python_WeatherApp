

def forecast(darksky_key, lat_lon_tuple, exclude):
    url = f'https://api.darksky.net/forecast/{secret_key}/{lat_lon_tuple[0]},{lat_lon_tuple[1]}?exclude={exclude}'
    response = requests.get(url)
    dictionary = json.dumps(response.json(), sort_keys=True, indent=4)
    return dictionary
