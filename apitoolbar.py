
from requests import get
import json

from requests import get
words = input("what would you like to translate to doge speak ")
word = words.replace(" ", "%20")
reponse = get('https://api.funtranslations.com/translate/doge.json?text=' + word)
transl = json.loads(reponse.content.decode())
print(transl)
''''
response = get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})

joke = json.loads(response.content.decode())


print(joke["joke"])
'''