from telethon import events
from os import remove
import modules.client

client = modules.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.sdmd'))
async def runsdmd(event):
    await event.delete()
    targetcontent = await event.get_reply_message()
    downloadtargetcontent = await targetcontent.download_media()
    send = await client.send_file("me", downloadtargetcontent)
    remove(downloadtargetcontent)