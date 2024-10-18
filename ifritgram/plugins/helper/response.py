import core.client
from os import environ
import utils
from utils import buttons
import docsdata
from docsdata import usages
from telethon import events
from telethon.tl.custom import Button

ifritgram_bot = core.client.ifritgram_bot
owner = int(environ["owner"])

@ifritgram_bot.on(events.CallbackQuery)
async def query_response(event):
    try:
        categories = buttons.categories_menu
        show_misc_menu = buttons.misc_menu
        back_misc_menu = buttons.back_misc
        user_id = event.original_update.user_id
        button_data = event.data
        if user_id == owner:
            if button_data == b'misc':
                await event.edit(f"{docsdata.misc}", buttons=show_misc_menu)
            elif button_data == b'back_misc':
                await event.edit(f"{docsdata.misc}", buttons=show_misc_menu)
            elif button_data == b'main_menu':
                await event.edit(f"🧞‍♂️ Ifritgram\n⚙️ Version: {utils.ifritgram_version}\nIfritgram's user manual is quite advanced, and the usage of all features is documented here.", buttons=categories)
            elif button_data == b'exit':
                await event.edit(f"Congratulations to you.\nI hope you have read all the uses of Ifritgram. If you forget the magic of Ifritgram, you will come back here and read the magic. And enjoy the hidden power forbidden by Telegram.", buttons=Button.clear())

            elif button_data == b'ping':
                await event.edit(usages.ping_usage, buttons=back_misc_menu, parse_mode="markdown")
            elif button_data == b'raid':
                await event.edit(usages.raid_usage, buttons=back_misc_menu, parse_mode="markdown")
        else:
            await event.answer("You don't have permission to access it; you need to deploy your own Ifritgram.", alert=True)
    except:
        pass