import core.client
from os import environ
from telethon import events
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.contacts import AddContactRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import BlockRequest

crowgram_assistant = core.client.crowgram_assistant
owner = int(environ["owner"])

@events.register(events.NewMessage(incoming=True, pattern=r"\>c"))
async def connect_user(event):
    try:
        if event.is_private:
            commander = event.original_update.user_id
            if commander == owner:
                await event.delete()
                get_action_details = event.message.raw_text.split()
                action_type = get_action_details[1]
                type_id = "-id"
                type_user_name = "-username"
                limit = 3
                command_limit = len(get_action_details)
                if command_limit == limit:
                    if action_type == type_id:
                        user_id = int(get_action_details[2])
                        contacts = await crowgram_assistant(GetContactsRequest(hash=0))
                        contacts_users_id = set([])
                        for user in contacts.users:
                            contacts_users_id.add(user.id)
                        if user_id not in contacts_users_id:
                            get_user_name = await crowgram_assistant(GetFullUserRequest(user_id))
                            first_name = get_user_name.users[0].first_name
                            last_name = get_user_name.users[0].last_name
                            if first_name and last_name:
                                await crowgram_assistant(AddContactRequest(
                                    id = user_id,
                                    first_name = first_name,
                                    last_name = last_name,
                                    phone = "",
                                    add_phone_privacy_exception = False
                                ))
                                await crowgram_assistant.send_message(commander, f"{first_name} is allowed to play music.")
                            elif first_name:
                                await crowgram_assistant(AddContactRequest(
                                    id = user_id,
                                    first_name = first_name,
                                    last_name = "",
                                    phone = "",
                                    add_phone_privacy_exception = False
                                ))
                                await crowgram_assistant.send_message(commander, f"{first_name} is allowed to play music.")
                            elif last_name:
                                await crowgram_assistant(AddContactRequest(
                                    id = user_id,
                                    first_name = "",
                                    last_name = last_name,
                                    phone = "",
                                    add_phone_privacy_exception = False
                                ))
                                await crowgram_assistant.send_message(commander, f"{last_name} is allowed to play music.")
                        elif user_id in contacts_users_id:
                            get_user_name = await crowgram_assistant(GetFullUserRequest(user_id))
                            first_name = get_user_name.users[0].first_name
                            if first_name:
                                await crowgram_assistant.send_message(commander, f"{first_name} has already been given permission to play music.")
                    elif action_type == type_user_name:
                        user_name = get_action_details[2]
                        get_user_details = await crowgram_assistant.get_entity(user_name)
                        user_id = get_user_details.id
                        contacts = await crowgram_assistant(GetContactsRequest(hash=0))
                        contacts_users_id = set([])
                        for user in contacts.users:
                            contacts_users_id.add(user.id)    
                        if user_id not in contacts_users_id:
                            first_name = get_user_details.first_name
                            last_name = get_user_details.last_name
                            if first_name and last_name:
                                await crowgram_assistant(AddContactRequest(
                                    id = user_id,
                                    first_name = first_name,
                                    last_name = last_name,
                                    phone = "",
                                    add_phone_privacy_exception = False
                                ))
                                await crowgram_assistant.send_message(commander, f"{first_name} is allowed to play music.")
                            elif first_name:
                                await crowgram_assistant(AddContactRequest(
                                    id = user_id,
                                    first_name = first_name,
                                    last_name = "",
                                    phone = "",
                                    add_phone_privacy_exception = False
                                ))
                                await crowgram_assistant.send_message(commander, f"{first_name} is allowed to play music.")
                            elif last_name:
                                await crowgram_assistant(AddContactRequest(
                                    id = user_id,
                                    first_name = "",
                                    last_name = last_name,
                                    phone = "",
                                    add_phone_privacy_exception = False
                                ))
                                await crowgram_assistant.send_message(commander, f"{last_name} is allowed to play music.")
                        elif user_id in contacts_users_id:
                            user_name = get_action_details[2]
                            get_user_details = await crowgram_assistant.get_entity(user_name)
                            first_name = get_user_details.first_name
                            if first_name:
                                await crowgram_assistant.send_message(commander, f"{first_name} has already been given permission to play music.")
                else:
                    await crowgram_assistant.send_message(commander, "The wrong command was given; please read the user manual.")
            else:
                crowgram_image = "https://telegra.ph/file/700b7f318d380cb2d228d.jpg"
                await crowgram_assistant.send_file(commander, crowgram_image, caption="You are not allowed to use this powerful command, yet you tried to do malicious activities using this command, so you were blocked by the automatic system.")
                await crowgram_assistant(BlockRequest(commander))
    except ValueError:
        await event.delete()
        commander = event.peer_id.user_id
        await crowgram_assistant.send_message(commander, "Something went wrong")
    except:
        pass