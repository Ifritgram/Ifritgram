from telethon import events
from wikipediaapi import Wikipedia
import modules.client

client = modules.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r"\.wiki"))
async def runwiki(event):
    await event.delete()
    userquestion = event.message.raw_text.splitlines()
    replacedata = userquestion[0].replace(".wiki ", "")
    process = replacedata.splitlines()
    messagelocation = event.to_id
    setlanguage = Wikipedia("en")
    page = setlanguage.page(f"{process[0]}")
    maincontent = page.summary[0:4096]
    await client.send_message(messagelocation, f"{maincontent}")
