import core.client
from telethon import events
from datetime import datetime

ifritgram = core.client.ifritgram

@events.register(events.NewMessage(outgoing=True, pattern=r"\>ping"))
async def ping_the_server(event):
    try:
        await event.delete()
        start = datetime.now()
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        chat = event.to_id
        await ifritgram.send_message(chat, f"Pinged!\nLatency: {ms} ms")
    except:
        pass