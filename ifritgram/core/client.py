from os import environ
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = int(environ["api_id"])
api_hash = environ["api_hash"]
string_session = environ["string_session"]

ifritgram = TelegramClient(StringSession(string_session), api_id, api_hash)