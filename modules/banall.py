from telethon import events


@events.register(events.NewMessage(outgoing=True, pattern=r"\.fba"))
async def runfba(event):
    await event.delete()
    messagelocation = event.to_id
    async for user in event.client.iter_participants(messagelocation):
        user_id = user.id
        try:
            await event.client.edit_permissions(
                messagelocation, user_id, view_messages=False
            )
        except:
            pass
