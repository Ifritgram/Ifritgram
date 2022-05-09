from telethon import events
import string
from random import sample


@events.register(events.NewMessage(outgoing=True, pattern=r"\.gpwd"))
async def rungpwd(event):
    await event.delete()
    lenght = event.message.raw_text.split()
    messagelocation = event.to_id
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    mixed = uppercase + lowercase + digits + punctuation
    generate = sample(mixed, int(lenght[1]))
    password = "".join(generate)
    await event.client.send_message(
        messagelocation, f"Password Is: {password}"
    )
