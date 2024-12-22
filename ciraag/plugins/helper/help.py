from ciraag.core.module_injector import *
from ciraag.core.client import ciraag_bot
from ciraag.core.custom_handler import handler
from ciraag.utils import buttons
from ciraag.utils import ciraag_version
from telethon import events
from telethon.errors.rpcerrorlist import ChatSendInlineForbiddenError

assistant_bot_username = environ["assistant_bot_username"]
owner_id = int(environ["owner_id"])

@Ciraag(rf"\{handler}help")
async def execute_helper(event):
    await event.delete()
    class Helper:
        async def run(self):
            try:
                self.chat = event.chat_id
                self.run_ciraag_helper = await ciraag.inline_query(f"{assistant_bot_username}", "help")
                await self.run_ciraag_helper[0].click(self.chat)
            except ChatSendInlineForbiddenError:
                self.get_group_details = await ciraag.get_entity(int(self.chat))
                self.chat_name = self.get_group_details.title
                await ciraag.send_message(self.chat, f"Inline message sending is currently disabled on {self.chat_name}. As a result, we are unable to display the Help menu within this chat.")
            except:
                pass

    user = Helper()
    await user.run()

@ciraag_bot.on(events.InlineQuery)
async def get_query(query):
    class UserQuery:
        async def response(self):
            try:
                if query.text == "help":
                    self.categories = buttons.categories_menu
                    self.build_help_article = query.builder.article(
                        title = "Ciraag",
                        text = f"🧞‍♂️ Ciraag\n⚙️ Version: {ciraag_version}\nCiraag's user manual is quite advanced, and the usage of all features is documented here.",
                        buttons = self.categories
                    )
                    await query.answer([self.build_help_article])
            except:
                pass
            
    helper = UserQuery()
    await helper.response()