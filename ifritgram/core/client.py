from os import environ
from telethon import TelegramClient
from telethon.sessions import StringSession

api_id = int(environ["api_id"])
api_hash = environ["api_hash"]
string_session = environ["string_session"]
bot_token = environ["bot_token"]

ifritgram = TelegramClient(StringSession(string_session), api_id, api_hash)
ifritgram_bot = TelegramClient("ifritgram", api_id, api_hash).start(bot_token=bot_token)