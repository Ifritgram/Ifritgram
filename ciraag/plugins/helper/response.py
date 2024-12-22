from ciraag.core.module_injector import *
from ciraag.core.client import ciraag_bot
from ciraag.utils import buttons
from ciraag.utils import ciraag_version
from ciraag.docs import misc
from ciraag.docs import usages
from telethon import events
from telethon.tl.custom import Button

@ciraag_bot.on(events.CallbackQuery)
async def query_response(event):
    class Activated:
        async def do_response(self):
            try:
                self.categories = buttons.categories_menu
                self.show_misc_menu = buttons.misc_menu
                self.back_misc_menu = buttons.back_misc
                self.user_id = event.original_update.user_id
                self.owner_id = int(environ["owner_id"])
                self.button_data = event.data

                if self.user_id == self.owner_id:
                    if self.button_data == b'misc':
                        await event.edit(f"{misc}", buttons=self.show_misc_menu)
                    elif self.button_data == b'back_misc':
                        await event.edit(f"{misc}", buttons=self.show_misc_menu)
                    elif self.button_data == b'main_menu':
                        await event.edit(f"🧞‍♂️ Ciraag\n⚙️ Version: {ciraag_version}\nCiraag's user manual is quite advanced, and the usage of all features is documented here.", buttons=self.categories)
                    elif self.button_data == b'exit':
                        await event.edit(f"Congratulations on your achievement!\nI hope you've explored the full potential of Ciraag. Should you need a refresher on its capabilities, please don't hesitate to revisit this guide. Discover the remarkable features and unlock the hidden power that sets Ciraag apart.", buttons=Button.clear())
                    
                    elif self.button_data == b'ping':
                        await event.edit(usages.ping_usage, buttons=self.back_misc_menu, parse_mode="markdown")
                    elif self.button_data == b'timer':
                        await event.edit(usages.self_destruct_usage, buttons=self.back_misc_menu, parse_mode="markdown")
                else:
                    await event.answer("You don't have permission to access it; you need to deploy your own Ciraag.", alert=True)
            except:
                pass
            
    helper = Activated()
    await helper.do_response()