from telethon import events
from time import sleep
import requests


@events.register(events.NewMessage(outgoing=True, pattern=r"\.zci"))
async def runzci(event):
    await event.edit("Searching...")
    sleep(2)
    await event.delete()
    getlocation = event.message.raw_text.split()
    messagelocation = event.to_id
    try:
        datainformation = (
            f"https://api.zippopotam.us/{getlocation[1]}/{getlocation[2]}"
        )
        getdata = requests.get(datainformation)
        maindata = getdata.json()
        postcode = maindata["post code"]
        country = maindata["country"]
        countryabbreviation = maindata["country abbreviation"]
        placename = maindata["places"][0]["place name"]
        placelongitude = maindata["places"][0]["longitude"]
        placelatitude = maindata["places"][0]["latitude"]
        placestate = maindata["places"][0]["state"]
        placestateabbreviation = maindata["places"][0]["state abbreviation"]
        await event.client.send_message(
            messagelocation,
            f"Post Code: {postcode}\nCountry: {country}\nCountry Abbreviation: {countryabbreviation}\nPlace Name: {placename}\nLongitude: {placelongitude}\nLatitude: {placelatitude}\nState: {placestate}\nState Abbreviation: {placestateabbreviation}",
        )
    except:
        pass
