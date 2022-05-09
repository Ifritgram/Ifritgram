from telethon import events


@events.register(events.NewMessage(outgoing=True, pattern=r"\.rm"))
async def runrm(event):
    await event.delete()
    getmessage = await event.get_reply_message()
    messagelocation = event.to_id
    try:
        await event.client.delete_messages(messagelocation, getmessage.id)
    except:
        pass
