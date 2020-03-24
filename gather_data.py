from darksky_API_call import forecast
from googlemaps_API_call import find_lat_and_lon
from keys import *

# exclude = 'minutely, hourly, daily, alerts, flags'

location = "CB215NX"

lat_lon = find_lat_and_lon(location, googlemaps_key)
forecast_data = forecast(darksky_key, lat_lon, exclude)

print(lat_lon)
print(forecast_data)
