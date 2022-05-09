from telethon import events


@events.register(events.NewMessage(outgoing=True, pattern=r"\.fka"))
async def runfka(event):
    await event.delete()
    messagelocation = event.to_id
    async for user in event.client.iter_participants(messagelocation):
        user_id = user.id
        ridogramuserdetails = await event.get_sender()
        try:
            if ridogramuserdetails.id == user_id:
                pass
            else:
                await event.client.kick_participant(messagelocation, user_id)
        except:
            pass
