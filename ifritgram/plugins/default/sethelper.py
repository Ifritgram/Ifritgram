import core.client
from os import environ
from telethon import events
from time import sleep
from telethon.tl.functions.channels import JoinChannelRequest

ifritgram = core.client.ifritgram
assistant_bot = environ["assistant_bot"]
ifritgram_chat = "@ifritgram_chat"
botfather = "@BotFather"

async def process(botfather, setup):
    try:
        await ifritgram.send_message(botfather, setup)
        await ifritgram.send_read_acknowledge(botfather)
        sleep(1)
        await ifritgram.send_read_acknowledge(botfather)
    except:
        pass

async def processing():
    try:
        await process(botfather, "/setinline")
        await process(botfather, f"{assistant_bot}")
        await process(botfather, "Ifritgram")
        await process(botfather, "/setabouttext")
        await process(botfather, f"{assistant_bot}")
        await process(botfather, "The assistant of the Ifritgram user for the purposes of @Ifritgram magic.")
        await process(botfather, "/setdescription")
        await process(botfather, f"{assistant_bot}")
        await process(botfather, "A powerful multi-featured userbot on Telegram.")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r"\>sethelper"))
async def set_helper(event):
    await event.edit("Processing...")
    try:
        await ifritgram(JoinChannelRequest(channel=f"{ifritgram_chat}"))
    except:
        pass
    await processing()
    await event.edit("Successfully setup the helper bot.")