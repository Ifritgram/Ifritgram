from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from ciraag.plugins.helper.setup_assistant import Helper
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import InviteRequestSentError

@Ciraag(rf"\{handler}setup")
async def set_helper(event):
    await event.edit("Thank you for your request. I've initiated the process of setting up Ciraag's Help Menu. Please allow me a few seconds to complete this task.")
    class Message:
        async def display(self):
            self.ciraag_user_details = await event.get_sender()
            self.user_first_name = self.ciraag_user_details.first_name
            self.ciraag_user_id = self.ciraag_user_details.id
            self.assistant_bot_username = environ["assistant_bot_username"]
            await event.edit(f"Good news, <a href='tg://user?id={self.ciraag_user_id}'>{self.user_first_name}</a>!\nYour Assistant Bot {self.assistant_bot_username} is now fully set up.", parse_mode="html")

    assistant = Helper()
    success = Message()
    
    try:
        await assistant.processing()
        await assistant.completed()
    except YouBlockedUserError:
        await ciraag(UnblockRequest(id="@BotFather"))
        await assistant.processing()
    except InviteRequestSentError:
        pass
    await success.display()