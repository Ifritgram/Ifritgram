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
            main_menu = core.helpers.display_menu
            show_help = query.builder.article(
                title = "🤖 Crowgram",
                text = f"🤖 Crowgram\n⚙️ Version: {utils.crowgram_version}\n\n📖 Crowgram's user manual is quite advanced, and the usage of all features is documented here.",
                buttons = main_menu
            )
            await query.answer([show_help])
    except:
        pass

@crowgram_bot.on(events.CallbackQuery)
async def help_response(event):
    try:
        main_menu = core.helpers.display_menu
        back_button = core.helpers.back
        checker = event.original_update.user_id
        button_data = event.data
        if checker == owner:
            if button_data == b'alive':
                await event.edit(utils.information.alive_usage, buttons=back_button)
            elif button_data == b'ping':
                await event.edit(utils.information.ping_usage, buttons=back_button)          
            elif button_data == b'id':
                await event.edit(utils.information.id_usage, buttons=back_button)     
            elif button_data == b'protection':
                await event.edit(utils.information.protection_usage, buttons=back_button)        
            elif button_data == b'restricted':
                await event.edit(utils.information.restricted_usage, buttons=back_button) 
            elif button_data == b'logger':
                await event.edit(utils.information.logger_usage, buttons=back_button)        
            elif button_data == b'player':
                await event.edit(utils.information.player_usage, buttons=back_button)
            elif button_data == b'who':
                await event.edit(utils.information.who_usage, buttons=back_button)           
            elif button_data == b'updater':
                await event.edit(utils.information.updater_usage, buttons=back_button)
            elif button_data == b'back':
                await event.edit(f"🤖 Crowgram\n⚙️ Version: {utils.crowgram_version}\n\n📖 Crowgram's user manual is quite advanced, and the usage of all features is documented here.", buttons=main_menu)
        else:
            await event.answer("You don't have permission to access it; you need to deploy your own Crowgram.", alert=True)
    except:
        pass