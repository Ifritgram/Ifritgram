from telethon import events
from time import sleep


@events.register(events.NewMessage(outgoing=True, pattern=r"\.rgm"))
async def runrgm(event):
    await event.edit("Recovering Delete Messages...")
    sleep(2)
    await event.delete()
    try:
        targetgroup = event.to_id
        recoveredplace = "me"
        grouplog = await event.client.get_admin_log(
            targetgroup, edit=False, delete=True
        )
        for restore in grouplog:
            await event.client.send_message(
                recoveredplace, restore.original.action.message, silent=True
            )
    except:
        pass
