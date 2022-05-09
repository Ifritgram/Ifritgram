from telethon import events
import random
from os import remove


@events.register(events.NewMessage(outgoing=True, pattern=r"\.tti"))
async def runtti(event):
    messagelocation = event.to_id
    repliedmessage = await event.get_reply_message()
    await event.edit("Processing...")
    targetbot = "@CarbonNowShBot"
    working = await event.client.get_entity(targetbot)
    filename = "generatebyridogram.png"
    try:
        async with event.client.conversation(working) as startconversation:
            await startconversation.send_message(repliedmessage)
            response = await startconversation.wait_event(
                events.MessageEdited(incoming=True, from_users=working.id)
            )
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            await response.click(row, column)
            response = await startconversation.wait_event(
                events.NewMessage(incoming=True, from_users=working.id)
            )
            carbon = response.message.media
            await event.client.download_media(carbon, filename)
            await event.delete()
            await event.client.send_file(messagelocation, filename)
            remove(filename)
    except:
        pass
