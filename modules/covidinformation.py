from telethon import events
from time import sleep
import requests
from bs4 import BeautifulSoup


@events.register(events.NewMessage(outgoing=True, pattern=r"\.covid"))
async def runcovid(event):
    await event.edit("Ridogram Collect Covid - 19 Data...")
    sleep(2)
    await event.delete()
    selectcountry = event.message.raw_text.split()
    messagelocation = event.to_id
    url = (
        f"https://www.worldometers.info/coronavirus/country/{selectcountry[1]}"
    )
    gethtmlcontent = requests.get(url)
    soup = BeautifulSoup(gethtmlcontent.text, "html.parser")
    maindata = ""
    for getcoviddata in soup.find("div", class_="content-inner").find_all(
        "span"
    ):
        maindata = maindata + " " + getcoviddata.get_text()
    createlist = maindata.split()
    covidcountryname = event.message.raw_text.split()
    usercountry = covidcountryname[1]
    countryname = usercountry.title()
    await event.client.send_message(
        messagelocation,
        f"Covid - 19 Information Of {countryname}\n\nTotal Cases: {createlist[0]}\nTotal Deaths: {createlist[1]}\nTotal Recovered: {createlist[2]}",
    )
