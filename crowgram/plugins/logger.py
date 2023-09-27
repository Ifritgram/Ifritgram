import core.client
import os
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest

crowgram = core.client.crowgram

@events.register(events.NewMessage)
async def get_pm_log(event):
    try:
        pm_log_location = int(os.environ["pm_log_location"])
        if pm_log_location:
            if event.is_private:
                get_crowgram_user_details = await crowgram(GetFullUserRequest("me"))
                crowgram_user_id = get_crowgram_user_details.users[0].id
                get_sender = await event.get_sender()
                sender_id = get_sender.id
                telegram = 777000
                get_sender_type = await event.get_chat()
                sender_type_id = get_sender_type.id
                type_information = await crowgram(GetFullUserRequest(sender_type_id))
                bot = type_information.users[0].bot
                if crowgram_user_id == sender_id:
                    pass
                elif sender_id == telegram:
                    pass
                elif bot:
                    pass
                else:
                    message = event.message
                    await crowgram.forward_messages(pm_log_location, message)
    except:
        pass

@events.register(events.NewMessage)
async def get_mention_log(event):
    try:
        mention_log_location = int(os.environ["mention_log_location"])
        if mention_log_location:
            mention = event.mentioned
            crowgram.parse_mode = "html"
            if mention == True:
                chat = await event.get_chat()
                chat_name = chat.title
                chat_id = chat.id
                user_id = event.from_id.user_id
                get_user_details = await crowgram(GetFullUserRequest(user_id))
                first_name = get_user_details.users[0].first_name
                last_name = get_user_details.users[0].last_name
                username = get_user_details.users[0].username
                message = event.message.message
                message_id = event.id
                source = f"<a href='https://t.me/c/{chat_id}/{message_id}'>View Message</a>"
                if not username:
                    if first_name and last_name:
                        await crowgram.send_message(mention_log_location, f"Chat Name: {chat_name}\n\nSender: {first_name} {last_name}\nSender User ID: {user_id}\nMessage Source: {source}\n\nMessage: {message}")
                    elif first_name:
                        await crowgram.send_message(mention_log_location, f"Chat Name: {chat_name}\n\nSender: {first_name}\nSender User ID: {user_id}\nMessage Source: {source}\n\nMessage: {message}")
                    elif last_name:
                        await crowgram.send_message(mention_log_location, f"Chat Name: {chat_name}\n\nSender: {last_name}\nSender User ID: {user_id}\nMessage Source: {source}\n\nMessage: {message}")
                else:
                    if first_name and last_name:
                        await crowgram.send_message(mention_log_location, f"Chat Name: {chat_name}\n\nSender: {first_name} {last_name}\nSender Username: @{username}\nSender User ID: {user_id}\nMessage Source: {source}\n\nMessage: {message}")
                    elif first_name:
                        await crowgram.send_message(mention_log_location, f"Chat Name: {chat_name}\n\nSender: {first_name}\nSender Username: @{username}\nSender User ID: {user_id}\nMessage Source: {source}\n\nMessage: {message}")
                    elif last_name:
                        await crowgram.send_message(mention_log_location, f"Chat Name: {chat_name}\n\nSender: {last_name}\nSender Username: @{username}\nSender User ID: {user_id}\nMessage Source: {source}\n\nMessage: {message}")
    except:
        pass