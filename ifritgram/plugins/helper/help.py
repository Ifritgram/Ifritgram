import core.client
from os import environ
import utils
from utils import buttons
from telethon import events
from telethon.errors.rpcerrorlist import ChatSendInlineForbiddenError

ifritgram = core.client.ifritgram
ifritgram_bot = core.client.ifritgram_bot
owner = int(environ["owner"])
assistant_bot = environ["assistant_bot"]

@events.register(events.NewMessage(outgoing=True, pattern=r"\>help"))
async def execute_helper(event):
    try:
        await event.delete()
        chat = event.chat_id
        run_ifritgram_helper = await ifritgram.inline_query(f"{assistant_bot}", "help")
        await run_ifritgram_helper[0].click(chat)
    except ChatSendInlineForbiddenError:
        get_group_details = await ifritgram.get_entity(int(chat))
        chat_name = get_group_details.title
        await ifritgram.send_message(chat, f"Inline message sending is not allowed on {chat_name}. This is why it is not possible to display the Help menu in this chat.")
    except:
        pass

@ifritgram_bot.on(events.InlineQuery)
async def get_query(query):
    if query.text == "help":
        categories = buttons.categories_menu
        build_help_article = query.builder.article(
            title = "Ifritgram",
            text = f"🧞‍♂️ Ifritgram\n⚙️ Version: {utils.ifritgram_version}\nIfritgram's user manual is quite advanced, and the usage of all features is documented here.",
            buttons = categories
        )
        await query.answer([build_help_article])