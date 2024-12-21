from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from datetime import datetime

@Ciraag(rf"\{handler}ping")
async def ping_the_server(event):
    await event.delete()
    class Ping:
        def __init__(self):
            self.start = datetime.now()
            self.end = datetime.now()
            self.ms = (self.end - self.start).microseconds / 1000
    server = Ping()
    chat = event.to_id
    await ciraag.send_message(chat, f"Pinged!\nLatency: {server.ms} ms")