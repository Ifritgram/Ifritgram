from os import environ
from telethon import TelegramClient
from telethon.sessions import StringSession

class Ciraag:
    def __init__(self):
        self.api_id = int(environ["api_id"])
        self.api_hash = environ["api_hash"]
        self.string_session = environ["string_session"]
        self.client = TelegramClient(StringSession(self.string_session), self.api_id, self.api_hash)

class CiraagHelper:
    def __init__(self):
        self.api_id = int(environ["api_id"])
        self.api_hash = environ["api_hash"]
        self.bot_token = environ["bot_token"]
        self.ciraag_client = TelegramClient("ciraag", self.api_id, self.api_hash).start(bot_token=self.bot_token)

ciraag = Ciraag().client
ciraag_bot = CiraagHelper().ciraag_client