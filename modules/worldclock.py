from telethon import events
from datetime import datetime
import pytz
from time import sleep


@events.register(events.NewMessage(outgoing=True, pattern=r"\.wc"))
async def runwc(event):
    await event.edit("Checking...")
    sleep(2)
    await event.delete()
    selectoption = event.message.raw_text.split()
    messagelocation = event.to_id
    try:
        if selectoption[1] == "show":
            localtimezone = pytz.timezone(f"{selectoption[2]}")
            localtime = datetime.now(localtimezone)
            currenttime = localtime.strftime("%I:%M %p")
            currentdate = localtime.strftime("%d %B %Y")
            await event.client.send_message(
                messagelocation,
                f"Today Is: {currentdate}\nCurrent Time: {currenttime}",
            )
        else:
            await event.client.send_message(messagelocation, "Wrong Option")
    except IndexError:
        await event.client.send_message(messagelocation, "Select An Option")
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
