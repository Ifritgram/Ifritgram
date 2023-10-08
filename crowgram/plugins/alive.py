import core.client
import utils
from telethon import events
from telethon import version
from platform import python_version

crowgram = core.client.crowgram

@events.register(events.NewMessage(outgoing=True, pattern=r"\>alive"))
async def check_alive(event):
    try:
        await event.delete()
        crowgram_user_details = await event.get_sender()
        first_name = crowgram_user_details.first_name
        crowgram_image = "https://telegra.ph/file/700b7f318d380cb2d228d.jpg"
        message_location = event.to_id
        await crowgram.send_file(message_location, crowgram_image, caption=f"Dear {first_name},\nI'm glad to announce that Crowgram is able to assist you.\n\n╭─⊸ Crowgram Version: {utils.crowgram_version}\n├─⊸ Python Version: {python_version()}\n╰─⊸ Telethon Version: {version.__version__}\n\nThank You,\nCrowgram")
    except:
        pass