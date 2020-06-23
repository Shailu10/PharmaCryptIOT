import urllib.request

websitedata=urllib.request.urlopen("https://api.thingspeak.com/channels/997798/feeds.json?api_key=42VRRZDFUAB0OWUD&results=50")
print(websitedata.read())

temprature=urllib.request.urlopen("https://api.thingspeak.com/channels/997798/fields/1.json?api_key=42VRRZDFUAB0OWUD&results=2")
print("\n\n",temprature.read())

humidity=urllib.request.urlopen("https://api.thingspeak.com/channels/997798/fields/2.json?api_key=42VRRZDFUAB0OWUD&results=2")
print("\n\n",humidity.read())

status=urllib.request.urlopen("https://api.thingspeak.com/channels/997798/status.json?api_key=42VRRZDFUAB0OWUD")
print("\n\n",status.read())