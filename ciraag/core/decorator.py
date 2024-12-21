from telethon import events

class Ciraag:
    def __init__(self, pattern):
        self.pattern = pattern
    def __call__(self, function):
        async def wrapper(event):
            await function(event)
        return events.register(events.NewMessage(outgoing=True, pattern=self.pattern))(wrapper)