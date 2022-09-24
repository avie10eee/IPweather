
from pprint import pprint
import requests
from requests import get
import json

response = ()
#ipify
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
#ipapi
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
'''print(location)'''


#openweathermap stuff
city = location["city"]
API_KEY = "ae81c5967df7adbdc65922f7f8e215e7"
base_url = "http://api.openweathermap.org/data/2.5/weather?&q="+city+"appid="+API_KEY
weather_data = requests.get(base_url).json()
pprint(weather_data)