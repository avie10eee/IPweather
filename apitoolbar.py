
from tkinter import N
from urllib import response
import requests
from requests import get
import json

ny = input("do you want to translate some thing y/n ")
if ny == "y":
    words = input("what would you like to translate to doge speak ")
    word = words.replace(" ", "%20")
    reponse = get('https://api.funtranslations.com/translate/doge.json?text=' + word)
    transl = json.loads(reponse.content.decode())
    print(transl["contents"]['translated'])


jy = input ("do you want a dad joke y/n ")
if jy == "y":
    respose = get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    joke = json.loads(respose.content.decode())
    print(joke["joke"])

yn = input("do you want know the mars weather y/n ")
if yn == "y":
    marsw = get ("https://api.nasa.gov/insight_weather/?api_key=XcdlNOSRAYU8OF96PKLLho7Ib7XwTO1V5EK1KeTe&feedtype=json&ver=1.0")
    print(json.loads(marsw.content.decode()))


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

apikey = 'A4xh9xli0h0y612bvtqsQIgnctKUh3X3'
tomorrow = Tomorrow(apikey, longitude=-location["longitude"], latitude=location["latitude"])
tomorrow.get_current(data_fields=['weatherCode'])


reponse = get("https://api.tomorrow.io/v4/")
transl = json.loads(reponse.content.decode())
print(transl["contents"]['translated'])
