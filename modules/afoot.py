import modules.client
from telethon import events
from telethon import version
from platform import python_version

client = modules.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.afoot'))
async def runafoot(event):
    await event.delete()
    ridogramuserdetails = await event.get_sender()
    messagelocation = event.to_id
    ridogramimage = "https://telegra.ph/file/5f0e2d045243c6ab2a4a0.jpg"
    await client.send_file(messagelocation, ridogramimage, caption=f"Dear {ridogramuserdetails.first_name},\nI'm glad to announce that Ridogram is able to assist you.\n\n╭─⊸ Ridogram Version: 0.23.5\n├─⊸ Python Version: {python_version()}\n╰─⊸ Telethon Version: {version.__version__}\n\nThank You,\nRidogram")