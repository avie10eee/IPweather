
from tkinter import N
from urllib import response
import requests
from requests import get
import json


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude")
    }
    return location_data
location = get_location()



################################
from tomorrow_io import Tomorrow

apikey = secrets.apikey
tomorrow = Tomorrow(apikey, longitude=-location["longitude"], latitude=location["latitude"])
tomorrow.get_current(data_fields=['weatherCode'])


reponse = get("https://api.tomorrow.io/v4/")
transl = json.loads(reponse.content.decode())
print(transl["contents"]['translated'])
