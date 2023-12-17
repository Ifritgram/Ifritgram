'''
Plugin Name: Help
Developer: iniridwanul
License: AGPL-3.0 license
'''

import core.client
import core.helpers
import utils
import utils.information
import os
from telethon import events

crowgram = core.client.crowgram
crowgram_bot = core.client.crowgram_bot
owner = int(os.environ["owner"])
assistant_bot = os.environ["assistant_bot"]

@events.register(events.NewMessage(outgoing=True, pattern=r"\>help"))
async def crowgram_help(event):
    try:
        await event.delete()
        message_location = event.chat_id
        run_help = await crowgram.inline_query(f"{assistant_bot}", "help")
        await run_help[0].click(message_location)
    except:
        pass

@crowgram_bot.on(events.InlineQuery)
async def get_query(query):
    try:
        if query.text == "help":
            categories = core.helpers.categories_menu
            show_help = query.builder.article(
                title = "🤖 Crowgram",
                text = f"🤖 Crowgram\n⚙️ Version: {utils.crowgram_version}\n\n📖 Crowgram's user manual is quite advanced, and the usage of all features is documented here.",
                buttons = categories
            )
            await query.answer([show_help])
    except:
        pass

@crowgram_bot.on(events.CallbackQuery)
async def help_response(event):
    try:
        categories = core.helpers.categories_menu
        show_misc_menu = core.helpers.misc_menu
        show_music_menu = core.helpers.music_menu
        back_misc_menu = core.helpers.back_misc
        back_music_menu = core.helpers.back_music
        checker = event.original_update.user_id
        button_data = event.data
        if checker == owner:
            if button_data == b'misc':
                await event.edit(buttons=show_misc_menu)
            elif button_data == b'music':
                await event.edit(buttons=show_music_menu)
            elif button_data == b'main_menu':
                await event.edit(buttons=categories)
            elif button_data == b'back_misc':
                await event.edit(f"🤖 Crowgram\n⚙️ Version: {utils.crowgram_version}\n\n📖 Crowgram's user manual is quite advanced, and the usage of all features is documented here.", buttons=show_misc_menu)
            elif button_data == b'alive':
                await event.edit(utils.information.alive_usage, buttons=back_misc_menu)
            elif button_data == b'ping':
                await event.edit(utils.information.ping_usage, buttons=back_misc_menu)          
            elif button_data == b'id':
                await event.edit(utils.information.id_usage, buttons=back_misc_menu)     
            elif button_data == b'protection':
                await event.edit(utils.information.protection_usage, buttons=back_misc_menu)        
            elif button_data == b'restricted':
                await event.edit(utils.information.restricted_usage, buttons=back_misc_menu) 
            elif button_data == b'logger':
                await event.edit(utils.information.logger_usage, buttons=back_misc_menu)        
            elif button_data == b'who':
                await event.edit(utils.information.who_usage, buttons=back_misc_menu)           
            elif button_data == b'updater':
                await event.edit(utils.information.updater_usage, buttons=back_misc_menu)
            elif button_data == b'back_music':
                await event.edit(f"🤖 Crowgram\n⚙️ Version: {utils.crowgram_version}\n\n📖 Crowgram's user manual is quite advanced, and the usage of all features is documented here.", buttons=show_music_menu)
            elif button_data == b'connect':
                await event.edit(utils.information.connect_usage, buttons=back_music_menu)
            elif button_data == b'disconnect':
                await event.edit(utils.information.disconnect_usage, buttons=back_music_menu)
            elif button_data == b'authorized':
                await event.edit(utils.information.authorized_usage, buttons=back_music_menu)
            elif button_data == b'play':
                await event.edit(utils.information.play_usage, buttons=back_music_menu)
            elif button_data == b'vplay':
                await event.edit(utils.information.vplay_usage, buttons=back_music_menu)
            elif button_data == b'pause':
                await event.edit(utils.information.pause_usage, buttons=back_music_menu)
            elif button_data == b'resume':
                await event.edit(utils.information.resume_usage, buttons=back_music_menu)
            elif button_data == b'end':
                await event.edit(utils.information.end_usage, buttons=back_music_menu)
        else:
            await event.answer("You don't have permission to access it; you need to deploy your own Crowgram.", alert=True)
    except:
        pass