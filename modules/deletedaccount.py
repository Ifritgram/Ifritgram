from telethon import events
from time import sleep


@events.register(events.NewMessage(outgoing=True, pattern=r"\.sda"))
async def runsda(event):
    await event.edit("Searching...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    deletedid = []
    try:
        chatname = event.chat.title
        async for users in event.client.iter_participants(messagelocation):
            if users.deleted:
                deletedid.append(users.id)
        countdeletedid = len(deletedid)
        if countdeletedid == 1:
            await event.client.send_message(
                messagelocation,
                f"{countdeletedid} Deleted Account Found In {chatname}",
            )
        elif countdeletedid == 0:
            await event.client.send_message(
                messagelocation, f"No Deleted Account Found In {chatname}"
            )
        else:
            await event.client.send_message(
                messagelocation,
                f"{countdeletedid} Deleted Accounts Found In {chatname}",
            )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )


@events.register(events.NewMessage(outgoing=True, pattern=r"\.rda"))
async def runrda(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    deletedid = []
    try:
        chatname = event.chat.title
        async for users in event.client.iter_participants(messagelocation):
            if users.deleted:
                deletedid.append(users.id)
                await event.client.kick_participant(messagelocation, users.id)
        countdeletedid = len(deletedid)
        if countdeletedid == 1:
            await event.client.send_message(
                messagelocation,
                f"{countdeletedid} Deleted Account Removed From {chatname}",
            )
        elif countdeletedid == 0:
            await event.client.send_message(
                messagelocation, f"No Deleted Account Found In {chatname}"
            )
        else:
            await event.client.send_message(
                messagelocation,
                f"{countdeletedid} Deleted Accounts Removed From {chatname}",
            )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
