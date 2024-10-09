from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = int(input("Enter API ID: "))
api_hash = input("Enter API Hash: ")

with TelegramClient(StringSession(), api_id, api_hash) as ifritgram:
    print(f"String Session: {ifritgram.session.save()}")
    ifritgram.send_message("me", ifritgram.session.save())