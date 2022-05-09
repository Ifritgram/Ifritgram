from telethon import events
from random import choice


@events.register(events.NewMessage(outgoing=True, pattern=r"\.gdm"))
async def rungdm(event):
    gdmwish = [
        "Life is a mystery and things always look impossible until it is made. Do not stop, move ahead and kill it. Good Morning, have a nice day!",
        "A very Good Morning! I hope this morning brings a bright smile on your face. May you have a beautiful and rewarding day! Always keep smiling.",
        "Good Morning! It is a bright day. Wake up every morning with an assurance that you can do it. Think positive, stay happy and keep going.",
        "Wishing you a very Good Morning!  A new blessing, a new hope, a new light and a new day is waiting for you to conquer it.",
        "Good morning! Always see the positive side of everything happening in your life.",
    ]
    randomgdmwish = choice(gdmwish)
    await event.edit(f"{randomgdmwish}")
