from telethon import events
from os import system

@events.register(events.NewMessage(outgoing=True, pattern=r"\>update"))
async def run_updater(event):
    await event.edit("Updating...")
    system("rm -rf *")
    system("git clone https://github.com/iniridwanul/Crowgram.git")
    system("cd Crowgram && cp -r * /app/ && rm -rf Crowgram")
    await event.edit("Successfully processed, wait a minute, and then type >alive")
    system("python3 crowgram.py")