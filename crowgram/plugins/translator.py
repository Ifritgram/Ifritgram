import core.client
from telethon import events
from googletrans import Translator

crowgram = core.client.crowgram

@events.register(events.NewMessage(outgoing=True, pattern=r"\>tr"))
async def run_translator(event):
    try:
        crowgram.parse_mode = "markdown"
        await event.edit("```Processing...```")
        get_destination = event.message.raw_text.split()
        destination_lenght = len(get_destination)
        validation = 2
        if event.reply_to:
            get_message = await event.get_reply_message()
            message = get_message.message
            if destination_lenght == validation:
                crowgram_translator = Translator()
                translate = crowgram_translator.translate(message, dest=f"{get_destination[1]}")
                translated_message = translate.text
                translated_source = translate.src
                translated_destination = translate.dest
                translated_pronunciation = translate.pronunciation
                if translated_pronunciation:
                    await event.edit(f"Translated from {translated_source} to {translated_destination} by Crowgram\nTranslated message: {translated_message}\nPronunciation: {translated_pronunciation}")
                else:
                    await event.edit(f"Translated from {translated_source} to {translated_destination} by Crowgram\nTranslated message: {translated_message}")
            else:
                await event.edit("Wrong Command")
        else:
            await event.edit("You need to reply to the message")
    except ValueError:
        await event.edit("Sorry, invalid destination language")
    except:
        pass