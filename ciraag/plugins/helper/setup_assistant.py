from ciraag.core.module_injector import *
from time import sleep
from telethon.tl.functions.channels import JoinChannelRequest

assistant_bot_username = environ["assistant_bot_username"]
ciraag_channel = "@ciraag"
ciraag_chat = "@ciraag_chat"
botfather = "@BotFather"

class Helper:
    async def process(self, botfather, setup):
        self.botfather = botfather
        self.setup = setup
        await ciraag.send_message(self.botfather, self.setup)
        await ciraag.send_read_acknowledge(self.botfather)
        sleep(1)
        await ciraag.send_read_acknowledge(self.botfather)
    
    async def processing(self):
        await self.process(botfather, "/setinline")
        await self.process(botfather, f"{assistant_bot_username}")
        await self.process(botfather, "Ciraag")
        await self.process(botfather, "/setabouttext")
        await self.process(botfather, f"{assistant_bot_username}")
        await self.process(botfather, "As the Assistant Bot for @Ciraag Userbot, I am integral to the functionality of @Ciraag User's help menu.")
        await self.process(botfather, "/setdescription")
        await self.process(botfather, f"{assistant_bot_username}")
        await self.process(botfather, "@Ciraag is an open-source Telegram userbot developed by the Python programming language and Telethon MTProto, a client library of the Telegram API, a secure and reliable way to interact with the Telegram platform.")
        await self.process(botfather, "/setuserpic")
        await self.process(botfather, f"{assistant_bot_username}")
        self.ciraag_logo = "assets/logo.png"
        await ciraag.send_file(botfather, self.ciraag_logo)
    
    async def completed(self):
        await ciraag(JoinChannelRequest(channel=f"{ciraag_channel}"))
        await ciraag(JoinChannelRequest(channel=f"{ciraag_chat}"))