
from pprint import pprint
import requests
from requests import get
import os

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
#print(location)


#openweathermap stuff
city = location["city"]
API_KEY = os.getenv("API_KEY")
#API_KEY = "80947e29d4714ff836e3ecc7d112f5e9"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
final_url = "base_url" + "appid=" + API_KEY + "&q=" + city
weather_data = requests.get(final_url).json()
print("\nCurrent Weather Data Of " + city +":\n")
pprint(weather_data)
