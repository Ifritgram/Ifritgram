import core.client
from os import environ
from utils import buttons, usages
from telethon import events

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
                await event.edit(buttons=show_misc_menu)
            elif button_data == b'back_misc':
                await event.edit(f"Ifritgram's user manual is quite advanced, and the usage of all features is documented here.", buttons=show_misc_menu)
            elif button_data == b'main_menu':
                await event.edit(buttons=categories)

            elif button_data == b'ping':
                await event.edit(usages.ping_usage, buttons=back_misc_menu, parse_mode="markdown")
        else:
            await event.answer("You don't have permission to access it; you need to deploy your own Ifritgram.", alert=True)
    except:
        pass