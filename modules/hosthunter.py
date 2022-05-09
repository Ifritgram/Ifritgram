from telethon import events
import socket


@events.register(events.NewMessage(outgoing=True, pattern=r"\.hh"))
async def runhh(event):
    await event.delete()
    messagelocation = event.to_id
    targethostname = event.message.raw_text.split()
    try:
        targethostip = socket.gethostbyname(targethostname[1])
        await event.client.send_message(
            messagelocation,
            f"Target Hostname: {targethostname[1]}\nFound IP: {targethostip}",
        )
    except:
        pass
