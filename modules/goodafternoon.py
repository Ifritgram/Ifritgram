from telethon import events
from random import choice


@events.register(events.NewMessage(outgoing=True, pattern=r"\.gda"))
async def rungda(event):
    gdawish = [
        "Over my head is a deep blue sky, and a relaxing wind. The significant and only thing, out of other things, I’m missing at the moment is your presence. Your company is GOLDEN to me. Have a pleasant afternoon.",
        "The afternoon comes with the brightness of the sun; the brightness which the sun brings reminds me of the light you have brought to my life. You are my happiness. I can’t wait any longer to have you in my arms again. I miss you so much, this afternoon.",
        "The gentle wind which comes with the afternoon feel like a warm and sweet hug from you, my Love. There’s nothing else in my thoughts apart from you, this bright afternoon. Hope you are having a great time?",
        "Do you know the time the sun shines at its fullness? It’s in the afternoon. It shows me how you brought light into my life, ever since I met you. I love you. Good afternoon.",
        "This is the time of the day when nature looks beautiful. I’m sure you wouldn’t want to miss the beauty displayed at this time. Wishing you a sweet afternoon.",
    ]
    randomgdawish = choice(gdawish)
    await event.edit(f"{randomgdawish}")
