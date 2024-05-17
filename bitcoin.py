import requests
import json
import pyttsx3

engine=pyttsx3.init()

r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data=json.loads(r.text)
bitcoin_price=data['bpi']['USD']['rate']
bitcoin_price=int(float(bitcoin_price.replace(',','')))
engine.say("bitcoin price is {}".format(bitcoin_price))
engine.runAndWait()

