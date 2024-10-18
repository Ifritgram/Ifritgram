import core.client
from telethon import events
from os import environ
from telethon.tl.functions.users import GetFullUserRequest
from os import remove

ifritgram = core.client.ifritgram
ifritgram_gallery = int(environ["ifritgram_gallery"])

@events.register(events.NewMessage(outgoing=True, pattern=r"\>tmd"))
async def get_self_destructive_media(event):
    await event.delete()
    try:
        chat = event.to_id
        if event.is_private:
            if event.reply_to:
                self_destruct = await event.get_reply_message()
                if self_destruct.media:
                     download_self_destruct_media = await self_destruct.download_media()
                     sender_id = self_destruct.sender_id
                     get_sender_details = await ifritgram(GetFullUserRequest(sender_id))
                     first_name = get_sender_details.users[0].first_name
                     developer =  "<a href='https://t.me/about_iniridwanul'>iniridwanul</a>"
                     ifritgram.parse_mode = "html"
                     await ifritgram.send_file(ifritgram_gallery, download_self_destruct_media, caption=f"Sender: {first_name}\nType: Self-destruct\nDeveloper: {developer}")
                     remove(download_self_destruct_media)
                else:
                     await ifritgram.send_message(chat, "If the message you want to collect is not media, please use the command in media.")
            else:
                await ifritgram.send_message(chat, "Please use the command in the media's reply.")
        else:
            await ifritgram.send_message(chat, "This feature only works for private messages.")
    except:
        pass