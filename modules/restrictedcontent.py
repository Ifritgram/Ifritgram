from telethon import events
from os import remove

@events.register(events.NewMessage(outgoing=True, pattern=r'\.rcd'))
async def rundrc(event):
    await event.delete()
    try:
        getrestrictedcontent = await event.get_reply_message()
        downloadrestrictedcontent = await getrestrictedcontent.download_media()
        await event.client.send_file("me", downloadrestrictedcontent)
        remove(downloadrestrictedcontent)
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.rts'))
async def runrts(event):
    await event.delete()
    try:
        foundrestrictedcontent = await event.get_reply_message()
        restricteddata = foundrestrictedcontent.message
        await event.client.send_message("me", restricteddata)
    except:
        pass