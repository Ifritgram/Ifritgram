import core.client
import utils.buttons
import utils.usages
import os
from telethon import events

ifritgram = core.client.ifritgram
ifritgram_bot = core.client.ifritgram_bot
owner = int(os.environ["owner"])
assistant_bot = os.environ["assistant_bot"]

@events.register(events.NewMessage(outgoing=True, pattern=r"\>help"))
async def ifritgram_helper(event):
    await event.delete()
    chat = event.chat_id
    run_ifritgram_helper = await ifritgram.inline_query(f"{assistant_bot}", "help")
    await run_ifritgram_helper[0].click(chat)

@ifritgram_bot.on(events.InlineQuery)
async def get_query(query):
    if query.text == "help":
        categories = utils.buttons.categories_menu
        build_help_article = query.builder.article(
            title = "Ifritgram",
            text = "Ifritgram's user manual is quite advanced, and the usage of all features is documented here.",
            buttons = categories
        )
        await query.answer([build_help_article])

@ifritgram_bot.on(events.CallbackQuery)
async def help_response(event):
    categories = utils.buttons.categories_menu
    show_misc_menu = utils.buttons.misc_menu
    back_misc_menu = utils.buttons.back_misc
    checker = event.original_update.user_id
    button_data = event.data
    if checker == owner:
        if button_data == b'misc':
            await event.edit(buttons=show_misc_menu)
        elif button_data == b'main_menu':
                await event.edit(buttons=categories)
        elif button_data == b'back_misc':
                await event.edit(f"Ifritgram's user manual is quite advanced, and the usage of all features is documented here.", buttons=show_misc_menu)
        elif button_data == b'ping':
                await event.edit(utils.usages.ping_usage, buttons=back_misc_menu)
    else:
        await event.answer("You don't have permission to access it; you need to deploy your own Ifritgram.", alert=True)