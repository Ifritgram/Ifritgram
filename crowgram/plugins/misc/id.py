'''
Plugin Name: ID
Developer: iniridwanul
License: AGPL-3.0 license
'''

import core.client
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest

crowgram = core.client.crowgram

@events.register(events.NewMessage(outgoing=True, pattern=r"\>id"))
async def get_id(event):
    await event.delete()
    get_username = event.message.raw_text.split()
    username_validation = len(get_username)
    no_username = 1
    data_lenght = 2
    command = ">id"
    message_location = event.to_id
    if username_validation == data_lenght:
        user_name = get_username[1]
        try:
            get_user_details = await crowgram(GetFullUserRequest(user_name))
            display_picture = get_user_details.users[0].photo
            if display_picture:
                first_name = get_user_details.users[0].first_name
                last_name = get_user_details.users[0].last_name
                user_id = get_user_details.users[0].id
                data_center = display_picture.dc_id
                if first_name and last_name:
                    await crowgram.send_message(message_location, f"Firstname: {first_name}\nLastname: {last_name}\nUser ID: {user_id}\nData Center: {data_center}")
                elif first_name:
                    await crowgram.send_message(message_location, f"Firstname: {first_name}\nUser ID: {user_id}\nData Center: {data_center}")
            else:
                first_name = get_user_details.users[0].first_name
                last_name = get_user_details.users[0].last_name
                user_id = get_user_details.users[0].id
                crowgram.parse_mode = "markdown"
                if first_name and last_name:
                    await crowgram.send_message(message_location, f"Firstname: {first_name}\nLastname: {last_name}\nUser ID: {user_id}")
                elif first_name:
                    await crowgram.send_message(message_location, f"Firstname: {first_name}\nUser ID: {user_id}")
        except ValueError:
            await crowgram.send_message(message_location, f"No user has @{user_name} as username")
        except:
            pass
    elif event.reply_to:
        get_information = await event.get_reply_message()
        user_id = get_information.sender_id
        get_reply_user_details = await crowgram(GetFullUserRequest(user_id))
        display_picture = get_reply_user_details.users[0].photo
        if display_picture:
            first_name = get_reply_user_details.users[0].first_name
            last_name = get_reply_user_details.users[0].last_name
            user_id = get_reply_user_details.users[0].id
            data_center = display_picture.dc_id
            if first_name and last_name:
                await crowgram.send_message(message_location, f"Firstname: {first_name}\nLastname: {last_name}\nUser ID: {user_id}\nData Center: {data_center}")
            elif first_name:
                await crowgram.send_message(message_location, f"Firstname: {first_name}\nUser ID: {user_id}\nData Center: {data_center}")
        else:
            first_name = get_reply_user_details.users[0].first_name
            last_name = get_reply_user_details.users[0].last_name
            user_id = get_reply_user_details.users[0].id
            if first_name and last_name:
                await crowgram.send_message(message_location, f"Firstname: {first_name}\nLastname: {last_name}\nUser ID: {user_id}")
            elif first_name:
                await crowgram.send_message(message_location, f"Firstname: {first_name}\nUser ID: {user_id}") 
    elif no_username == username_validation:
        if command == get_username[0]:
            fetch_chat_id = event.chat_id
            message_location = event.to_id
            await crowgram.send_message(message_location, f"This chat's ID is: {fetch_chat_id}")
    else:
        await crowgram.send_message(message_location, "Something went wrong")