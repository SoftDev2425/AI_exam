from geopy.geocoders import Nominatim
import certifi
import ssl
import time
import os

def get_coordinates(address, postnr):
    os.environ['SSL_CERT_FILE'] = certifi.where()
    geolocator = Nominatim(user_agent="PyHousr", ssl_context=ssl.create_default_context(cafile=certifi.where()))
    location = geolocator.geocode(f'{address} {postnr} Danmark')
    time.sleep(1)
    if location is not None:
        x = location.latitude
        y = location.longitude
    else:
        x = None
        y = None

    return x, y
