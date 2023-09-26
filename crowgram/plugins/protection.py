import core.client
from telethon import events
from telethon.tl.functions.contacts import AddContactRequest
from telethon.tl.functions.contacts import DeleteContactsRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.users import GetFullUserRequest

crowgram = core.client.crowgram

@events.register(events.NewMessage(outgoing=True, pattern=r"\>a"))
async def add_contact(event):
    try:
        crowgram.parse_mode = "markdown"
        await event.edit("```Processing...```")
        if event.reply_to:
            get_user_details = await event.get_reply_message()
            user_id = get_user_details.peer_id.user_id
            contacts = await crowgram(GetContactsRequest(hash=0))
            contacts_users_id = set([])
            for user in contacts.users:
                contacts_users_id.add(user.id)   
            if user_id not in contacts_users_id:
                get_user_name = await crowgram(GetFullUserRequest(user_id))
                first_name = get_user_name.users[0].first_name
                last_name = get_user_name.users[0].last_name
                if first_name and last_name:
                    await crowgram(AddContactRequest(
                        id = user_id,
                        first_name = first_name,
                        last_name = last_name,
                        phone = "",
                        add_phone_privacy_exception = False
                    ))
                    await event.edit("This user has been successfully approved")
                elif first_name:
                    await crowgram(AddContactRequest(
                        id = user_id,
                        first_name = first_name,
                        last_name = "",
                        phone = "",
                        add_phone_privacy_exception = False
                    ))
                    await event.edit("This user has been successfully approved")           
                elif last_name:
                    await crowgram(AddContactRequest(
                        id = user_id,
                        first_name = "",
                        last_name = last_name,
                        phone = "",
                        add_phone_privacy_exception = False
                    ))
                    await event.edit("This user has been successfully approved")
            elif user_id in contacts_users_id:
                await event.edit("This user is already approved")
        else:
            await event.edit("You need to reply to the message")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r"\>d"))
async def delete_contact(event):
    try:
        crowgram.parse_mode = "markdown"
        await event.edit("```Processing...```")
        if event.reply_to:
            get_user_details = await event.get_reply_message()
            get_user_id = [get_user_details.peer_id.user_id]
            user_id = get_user_id[0]
            contacts = await crowgram(GetContactsRequest(hash=0))
            contacts_users_id = set([])
            for user in contacts.users:
                contacts_users_id.add(user.id)
            if user_id in contacts_users_id:
                await crowgram(DeleteContactsRequest(id=get_user_id))
                await event.edit("This user has been successfully removed from the approved list")
            elif user_id not in contacts_users_id:
                await event.edit("This user is not already approved")
        else:
            await event.edit("You need to reply to the message")
    except:
        pass

@events.register(events.NewMessage)
async def checking(event):
    try:
        if event.is_private:
            who_is = event.peer_id.user_id
            who_is_type = await event.get_chat()
            bot = who_is_type.bot
            telegram = 777000
            find_user = await crowgram(GetFullUserRequest("me"))
            crowgram_user = find_user.users[0].id
            sender = await event.get_sender()
            sender_id = sender.id
            contacts = await crowgram(GetContactsRequest(hash=0))
            contacts_users_id = set([])
            for user in contacts.users:
                contacts_users_id.add(user.id)
            if who_is not in contacts_users_id:
                if who_is == crowgram_user:
                    pass
                elif sender_id == crowgram_user:
                    pass
                elif bot:
                    pass
                elif who_is == telegram:
                    pass
                else:
                    crowgram_image = "https://telegra.ph/file/700b7f318d380cb2d228d.jpg"
                    await crowgram.send_file(who_is, crowgram_image, caption="Thank you for sending me a message but I'm blocking you temporarily because I'm not allowing you to send me a message so please wait for my permission.")
                    await crowgram(BlockRequest(who_is))
    except:
        pass