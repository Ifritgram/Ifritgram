from telethon import events
import requests


@events.register(events.NewMessage(outgoing=True, pattern=r"\.mpt"))
async def runmpt(event):
    await event.edit("Checking...")
    messagelocation = event.to_id
    getlocation = event.message.raw_text.splitlines()
    replacedata = getlocation[0].replace(".mpt ", "")
    userlocation = replacedata.splitlines()
    prayerimage = "http://telegra.ph/file/dc498f7c4ca7afc52d0ee.jpg"
    try:

        class getprayertimeinformation:
            salatupdate = f"http://muslimsalat.com/{userlocation[0]}.json"
            getdata = requests.get(salatupdate)
            maindata = getdata.json()

        salatdata = getprayertimeinformation()
        if salatdata.maindata["status_description"] == "Failed.":
            await event.delete()
            await event.client.send_message(
                messagelocation, "Location Not Found"
            )
        else:
            salatdate = salatdata.maindata["items"][0]["date_for"]
            salatstate = salatdata.maindata["state"]
            salatcountry = salatdata.maindata["country"]
            salatcountrycode = salatdata.maindata["country_code"]
            sunrise = salatdata.maindata["items"][0]["shurooq"]
            fajr = salatdata.maindata["items"][0]["fajr"]
            dhuhr = salatdata.maindata["items"][0]["dhuhr"]
            asr = salatdata.maindata["items"][0]["asr"]
            maghrib = salatdata.maindata["items"][0]["maghrib"]
            isha = salatdata.maindata["items"][0]["isha"]
            await event.delete()
            await event.client.send_file(
                messagelocation,
                prayerimage,
                caption=f"Date: {salatdate}\nState: {salatstate}\nCountry: {salatcountry}\nCountry Code: {salatcountrycode}\nSunrise: {sunrise.upper()}\nFajr: {fajr.upper()}\nDhuhr: {dhuhr.upper()}\nAsr: {asr.upper()}\nMaghrib: {maghrib.upper()}\nIsha: {isha.upper()}",
            )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
