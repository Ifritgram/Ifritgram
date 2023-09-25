import core.client
from telethon import events

crowgram = core.client.crowgram

@events.register(events.NewMessage(outgoing=True, pattern=r"\>id"))
async def get_id(event):
    try:
        await event.delete()
        crowgram.parse_mode = "markdown"
        fetch_chat_id = event.chat_id
        message_location = event.to_id
        await crowgram.send_message(message_location, f"This chat's ID is: ```{fetch_chat_id}```")
    except:
        pass