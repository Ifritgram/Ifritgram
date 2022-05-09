from telethon import events
from telethon.tl.functions.photos import DeletePhotosRequest


@events.register(events.NewMessage(outgoing=True, pattern=r"\.rmdps"))
async def runrmdps(event):
    userdp = await event.client.get_profile_photos("me")
    await event.client(DeletePhotosRequest(userdp))
