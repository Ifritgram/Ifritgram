from telethon import events
from time import sleep
from telethon.tl.types import ChannelParticipantsAdmins


@events.register(events.NewMessage(outgoing=True, pattern=r"\.sa"))
async def runsa(event):
    await event.edit("Checking...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    adminname = []
    adminusername = []
    try:
        chatname = event.chat.title
        async for user in event.client.iter_participants(
            messagelocation, filter=ChannelParticipantsAdmins
        ):
            adminname.append(f"👤 {user.first_name}")
            adminusername.append(f"🔗 @{user.username}")
        if len(adminname) == 1:
            convertname = "\n".join(adminname)
            convertusername = "\n".join(adminusername)
            await event.client.send_message(
                messagelocation,
                f"Admin in {chatname}\n\nAdministrator Name:\n{convertname}\n\nAdministrator Username:\n{convertusername}",
            )
        else:
            convertname = "\n".join(adminname)
            convertusername = "\n".join(adminusername)
            await event.client.send_message(
                messagelocation,
                f"Admins in {chatname}\n\nAdministrators Name:\n{convertname}\n\nAdministrators Username:\n{convertusername}",
            )
    except:
        pass
