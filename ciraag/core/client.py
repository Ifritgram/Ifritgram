from os import environ
from telethon import TelegramClient
from telethon.sessions import StringSession

class Ciraag:
    def __init__(self):
        self.api_id = int(environ["api_id"])
        self.api_hash = environ["api_hash"]
        self.string_session = environ["string_session"]
        self.client = TelegramClient(StringSession(self.string_session), self.api_id, self.api_hash)

ciraag = Ciraag().client