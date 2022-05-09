from telethon import events
from time import sleep
import requests


@events.register(events.NewMessage(outgoing=True, pattern=r"\.fd"))
async def runfd(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        datainformation = "https://randomuser.me/api/"
        getdata = requests.get(datainformation)
        maindata = getdata.json()
        namet = maindata["results"][0]["name"]["title"]
        namef = maindata["results"][0]["name"]["first"]
        namel = maindata["results"][0]["name"]["last"]
        fakegender = maindata["results"][0]["gender"]
        fakelocationc = maindata["results"][0]["location"]["city"]
        fakelocations = maindata["results"][0]["location"]["state"]
        fakelocationp = maindata["results"][0]["location"]["postcode"]
        fakecountry = maindata["results"][0]["location"]["country"]
        fakeemail = maindata["results"][0]["email"]
        await event.client.send_message(
            messagelocation,
            f"Title: {namet}\nFirstname: {namef}\nLastname: {namel}\nGender: {fakegender}\nCity: {fakelocationc}\nState: {fakelocations}\nPostcode: {fakelocationp}\nCountry: {fakecountry}\nEmail: {fakeemail}",
        )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
