from telethon import events
from random import choice


@events.register(events.NewMessage(outgoing=True, pattern=r"\.gdn"))
async def rungdn(event):
    gdnwish = [
        "No matter how bad the day was, always try to end it with positive thoughts. Try to focus on the next day and hope for a sweet dream. Good night.",
        "No need to be upset or feel lonely tonight. Feel the calmness of this night with all your heart. Relax and have a tight sleep. Good night.",
        "You have so many reasons to thank God, but first thank him for such a peaceful night like this. What a blissful night for a good sleep. Good night!",
        "May you have sound sleep and wake up tomorrow with new hopes and a lot of positive energy. Good night to you!",
        "For me, the only truth in life is you and your love. When I wake up every morning, all I want is you to start over a new day. Good night!",
    ]
    randomgdnwish = choice(gdnwish)
    await event.edit(f"{randomgdnwish}")
