from telethon import events
from time import sleep
from urllib.request import urlopen
import json


@events.register(events.NewMessage(outgoing=True, pattern=r"\.iptrace"))
async def runiptrace(event):
    getip = event.message.raw_text.split()
    messagelocation = event.to_id
    await event.edit("Tracing...")
    sleep(2)
    await event.delete()
    targetip = getip[1]
    url = "http://ip-api.com/json/"
    start = urlopen(url + targetip)
    ipdata = start.read()
    information = json.loads(ipdata)
    await event.client.send_message(
        messagelocation,
        f"Target IP: {information['query']}\nCountry: {information['country']}\nCountry Code: {information['countryCode']}\nRegion: {information['region']}\nRegion Name: {information['regionName']}\nCity: {information['city']}\nZip: {information['zip']}\nLatitude: {information['lat']}\nLongitude: {information['lon']}\nTimezone: {information['timezone']}\nISP: {information['isp'].title()}\nOrganization: {information['org'].title()}\nASN: {information['as']}\n",
    )
