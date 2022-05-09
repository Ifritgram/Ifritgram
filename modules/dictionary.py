from telethon import events
from time import sleep
import requests


@events.register(events.NewMessage(outgoing=True, pattern=r"\.wm"))
async def runwm(event):
    await event.edit("Searching...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    getwords = event.message.raw_text.splitlines()
    replacedata = getwords[0].replace(".wm ", "")
    userwords = replacedata.splitlines()
    try:
        datainformation = (
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{userwords[0]}"
        )
        getdata = requests.get(datainformation)
        maindata = getdata.json()
        targetword = maindata[0]["word"]
        partofspeech = maindata[0]["meanings"][0]["partOfSpeech"]
        targetdefinitions = maindata[0]["meanings"][0]["definitions"][0][
            "definition"
        ]
        await event.client.send_message(
            messagelocation,
            f"Word: {targetword}\nPart Of Speech: {partofspeech}\nDefinition: {targetdefinitions}",
        )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
