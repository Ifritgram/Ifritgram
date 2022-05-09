from telethon import TelegramClient
from telethon.sessions import StringSession
import os

api_id = int(os.environ["api_id"])
api_hash = os.environ["api_hash"]
string = os.environ["string"]

client = TelegramClient(StringSession(string), api_id, api_hash)
