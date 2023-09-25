import core.client
from telethon import events
from datetime import datetime

crowgram = core.client.crowgram

@events.register(events.NewMessage(outgoing=True, pattern=r"\>ping"))
async def pinged(event):
    try:
        crowgram.parse_mode = "markdown"
        await event.edit("```Processing...```")
        message_location = event.to_id
        start = datetime.now()
        await event.delete()
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await crowgram.send_message(message_location, f"Pinged!\nLatency: {ms} ms")
    except:
        pass