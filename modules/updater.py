from telethon import events
from os import system


@events.register(events.NewMessage(outgoing=True, pattern=r"\.update"))
async def runupdate(event):
    await event.edit("Temporarily Updating...")
    system("rm -rf *")
    system("git clone https://github.com/iniridwanul/Ridogram.git")
    system("cd Ridogram && cp -r * /app/ && rm -rf Ridogram")
    await event.edit(
        "Successfully Processed, Wait A Minute And Then Type .afoot"
    )
    system("python3 ridogram.py")
