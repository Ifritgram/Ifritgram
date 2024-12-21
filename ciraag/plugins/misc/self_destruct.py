from ciraag.core.module_injector import *
from ciraag.core.custom_handler import handler
from telethon.tl.functions.users import GetFullUserRequest
from os import remove

@Ciraag(rf"\{handler}tmd")
async def get_self_destructive_media(event):
    await event.delete()
    class SelfDestruct:
        async def save(self):
            self.chat = event.to_id
            if event.is_private:
                if event.reply_to:
                    self.self_destruct = await event.get_reply_message()
                    if self.self_destruct.media:
                        self.download_self_destruct_media = await self.self_destruct.download_media()
                        self.sender_id = self.self_destruct.sender_id
                        self.get_sender_details = await ciraag(GetFullUserRequest(self.sender_id))
                        self.first_name = self.get_sender_details.users[0].first_name
                        self.developer =  "<a href='https://t.me/about_iniridwanul'>iniridwanul</a>"
                        self.gallery = int(environ["ciraag_gallery"])
                        await ciraag.send_file(self.gallery, self.download_self_destruct_media, caption=f"Sender: {self.first_name}\nType: Self-destruct\nDeveloper: {self.developer}", parse_mode="html")
                        remove(self.download_self_destruct_media)
                    else:
                        await ciraag.send_message(self.chat, "This function is specifically designed for downloading media files. Since the content you're attempting to download does not fall under the media category, please restrict the use of this feature to media files only.")
                else:
                    await ciraag.send_message(self.chat, "Please use the command in the media's reply.")
            else:
                await ciraag.send_message(self.chat, "This feature only works for private messages.")

    media = SelfDestruct()
    await media.save()