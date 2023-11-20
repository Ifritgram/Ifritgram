'''
Plugin Name: Set Helper
Developer: iniridwanul
License: AGPL-3.0 license
'''

import core.client
from os import environ
from telethon import events
from time import sleep
from telethon.tl.functions.channels import JoinChannelRequest

crowgram = core.client.crowgram
assistant_bot = environ["assistant_bot"]
crowgram_chat = "@CrowgramChat"

async def process(botfather, setup):
    try:
        await crowgram.send_message(botfather, setup)
        await crowgram.send_read_acknowledge(botfather)
        sleep(1)
    except:
        pass

async def processing():
    try:
        botfather = "@BotFather"
        await process(botfather, "/setinline")
        await process(botfather, f"{assistant_bot}")
        await process(botfather, "Crowgram")
        await process(botfather, "/setabouttext")
        await process(botfather, f"{assistant_bot}")
        await process(botfather, "The assistant of the Crowgram user for the purposes of @Crowgram magic.")
        await process(botfather, "/setdescription")
        await process(botfather, f"{assistant_bot}")
        await process(botfather, "@Crowgram is a powerful, advanced, multi-featured Telegram userbot.")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r"\>sethelper"))
async def set_helper(event):
    crowgram.parse_mode = "markdown"
    await event.edit("```Processing...```")
    try:
        await crowgram(JoinChannelRequest(channel=f"{crowgram_chat}"))
    except:
        pass
    await processing()
    await event.edit("Successfully setup @Crowgram's Assistant bot.")