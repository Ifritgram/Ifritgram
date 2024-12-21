from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from os import system

class Generate:
    def __init__(self):
        self.api_id = int(input("Enter App API ID: "))
        self.api_hash = input("Enter App API Hash: ")
        with TelegramClient(StringSession(), self.api_id, self.api_hash) as ciraag:
            ciraag.send_message("me", ciraag.session.save())
            system("clear")
            print("Dear Ciraag user,\nWe are pleased to inform you that your String Season Generation has been successfully completed. Please check your saved messages chat on Telegram. Your generated String Season has been sent to you there.\n\nSincerely,\nCiraag")

string_session = Generate()