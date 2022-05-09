from telethon import events
from datetime import datetime


@events.register(events.NewMessage(outgoing=True, pattern=r"\.ping"))
async def runping(event):
    await event.edit("Processing...")
    messagelocation = event.to_id
    try:
        start = datetime.now()
        await event.delete()
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.client.send_message(
            messagelocation, f"Pinged!\nLatency: {ms} ms"
        )
    except:
        pass
