import core.client
from telethon import events
from os import remove

crowgram = core.client.crowgram

@events.register(events.NewMessage(outgoing=True, pattern=r"\>rcd"))
async def get_restricted_content(event):
    try:
        await event.delete()
        get_command = event.message.raw_text.split()
        command_lenght = len(get_command)
        required_argument = 4
        public_type = "-public"
        private_type = "-private"
        answerable = 1
        if command_lenght == required_argument:
            get_type = get_command[1]
            public_link = get_command[2]
            private_id = f"-100{get_command[2]}"
            message_id = get_command[3]
            if get_type == public_type:
                get_data = await crowgram.get_messages(public_link, ids=int(message_id))
                if get_data.media and get_data.text:
                    download_target_content = await get_data.download_media()
                    await crowgram.send_file("me", download_target_content, caption=f"{get_data.text}")
                    remove(download_target_content)
                elif get_data.media:
                    download_target_content = await get_data.download_media()
                    await crowgram.send_file("me", download_target_content)
                    remove(download_target_content)
                elif get_data.text:
                    await crowgram.send_message("me", get_data.text)
            elif get_type == private_type:
                get_data = await crowgram.get_messages(int(private_id), ids=int(message_id))
                if get_data.media and get_data.text:
                    download_target_content = await get_data.download_media()
                    await crowgram.send_file("me", download_target_content, caption=f"{get_data.text}")
                    remove(download_target_content)
                elif get_data.media:
                    download_target_content = await get_data.download_media()
                    await crowgram.send_file("me", download_target_content)
                    remove(download_target_content)
                elif get_data.text:
                    await crowgram.send_message("me", get_data.text)
            else:
                await crowgram.send_message("me", "Wrong Argument")
        elif command_lenght == answerable:
            if event.reply_to:
                target_content = await event.get_reply_message()
                if target_content.media and target_content.text:
                    download_target_content = await target_content.download_media()
                    await crowgram.send_file("me", download_target_content, caption=f"{target_content.text}")
                    remove(download_target_content)
                elif target_content.text:
                    await crowgram.send_message("me", target_content.text)
                elif target_content.media:
                    download_target_content = await target_content.download_media()
                    await crowgram.send_file("me", download_target_content)
                    remove(download_target_content)
            else:
                await crowgram.send_message("me", "You need to reply to the message")
        else:
            await crowgram.send_message("me", "Wrong Command")
    except:
        pass