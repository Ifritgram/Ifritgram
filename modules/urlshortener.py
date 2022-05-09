from telethon import events
import pyshorteners
from time import sleep


@events.register(events.NewMessage(outgoing=True, pattern=r"\.us"))
async def runus(event):
    await event.edit("URL Shortening...")
    sleep(2)
    await event.delete()
    mainlink = event.message.raw_text.split()
    messagelocation = event.to_id
    try:
        shortener = pyshorteners.Shortener()
        shortening = shortener.tinyurl.short(f"{mainlink[1]}")
        await event.client.send_message(
            messagelocation, f"Shorturl: {shortening}"
        )
    except:
        pass
