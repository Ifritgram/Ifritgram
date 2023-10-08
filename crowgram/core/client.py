from telethon import TelegramClient
from telethon.sessions import StringSession
import os
from pytgcalls import PyTgCalls

api_id = int(os.environ["api_id"])
api_hash = os.environ["api_hash"]
string = os.environ["string"]
bot_token = os.environ["bot_token"]

assistant_api_id = int(os.environ["assistant_api_id"])
assistant_api_hash = os.environ["assistant_api_hash"]
assistant_string = os.environ["assistant_string"]

crowgram = TelegramClient(StringSession(string), api_id, api_hash)
crowgram_bot = TelegramClient("crowgram", api_id, api_hash).start(bot_token=bot_token)
crowgram_assistant = TelegramClient(StringSession(assistant_string), assistant_api_id, assistant_api_hash)
crowgram_call = PyTgCalls(crowgram_assistant)
crowgram_call.start()