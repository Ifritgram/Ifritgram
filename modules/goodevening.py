from telethon import events
from random import choice


@events.register(events.NewMessage(outgoing=True, pattern=r"\.gde"))
async def rungde(event):
    gdewish = [
        "Good evening! I hope you had a good and productive day. Cheer up!",
        "No matter how bad your day has been, the beauty of the setting sun will make everything serene. Good evening.",
        "Good evening dear. Thank you for making my evenings so beautiful and full of love.",
        "May the setting sun take down all your sufferings with it and make you hopeful for a new day. Good evening!",
        "Evening is a good time to look back at your day and think about all the things that you have done. Enjoy your evening with positive thoughts.",
    ]
    randomgdewish = choice(gdewish)
    await event.edit(f"{randomgdewish}")
