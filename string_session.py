#!/venv/bin/python3
import os # for installing telethon

try:
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
except:
    print("Setting up virtual environment...")
    if not os.path.isdir("venv"):
        os.system("python3 -m venv venv");
    os.system("venv/bin/pip3 install telethon")

api_id = int(input("Enter API ID: "))
api_hash = input("Enter API Hash: ")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())