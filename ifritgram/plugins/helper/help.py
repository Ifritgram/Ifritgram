import core.client
from os import environ
from utils import buttons
from telethon import events

ifritgram = core.client.ifritgram
ifritgram_bot = core.client.ifritgram_bot
owner = int(environ["owner"])
assistant_bot = environ["assistant_bot"]

@events.register(events.NewMessage(outgoing=True, pattern=r"\>help"))
async def execute_helper(event):
    await event.delete()
    chat = event.chat_id
    run_ifritgram_helper = await ifritgram.inline_query(f"{assistant_bot}", "help")
    await run_ifritgram_helper[0].click(chat)

@ifritgram_bot.on(events.InlineQuery)
async def get_query(query):
    if query.text == "help":
        categories = buttons.categories_menu
        build_help_article = query.builder.article(
            title = "Ifritgram",
            text = "Ifritgram's user manual is quite advanced, and the usage of all features is documented here.",
            buttons = categories
        )
        await query.answer([build_help_article])