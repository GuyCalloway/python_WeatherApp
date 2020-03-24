from darksky_API_call import forecast
from googlemaps_API_call import find_lat_and_lon
from keys import *

exclude = 'minutely, hourly, daily, alerts, flags'
lat_long_tuple = (-79.3892455, 43.6425701)

# data1 = find_lat_and_lon(location, googlemaps_key)
data2 = forecast(darksky_key, lat_lon_tuple, exclude)

print(data2)
