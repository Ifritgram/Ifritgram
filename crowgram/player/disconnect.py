import core.client
from os import environ
from telethon import events
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import DeleteContactsRequest
from telethon.tl.functions.contacts import BlockRequest

crowgram_assistant = core.client.crowgram_assistant
owner = int(environ["owner"])

@events.register(events.NewMessage(incoming=True, pattern=r"\>r"))
async def disconnect_user(event):
    try:
        if event.is_private:
            commander = event.original_update.user_id
            if commander == owner:
                await event.delete()
                get_user = event.message.raw_text.split()
                limit = 2
                command_lenght = len(get_user)
                if command_lenght == limit:
                    user_id = int(get_user[1])
                    target_user = [user_id]
                    contacts = await crowgram_assistant(GetContactsRequest(hash=0))
                    contacts_users_id = set([])
                    for user in contacts.users:
                        contacts_users_id.add(user.id)
                    get_user_name = await crowgram_assistant(GetFullUserRequest(user_id))
                    first_name = get_user_name.users[0].first_name
                    if user_id in contacts_users_id:
                        await crowgram_assistant(DeleteContactsRequest(id=target_user))
                        await crowgram_assistant.send_message(commander, f"{first_name}'s permission to play music has been revoked.")
                    else:
                        await crowgram_assistant.send_message(commander, f"{first_name}'s permission to play music has already been revoked, so there is no need to revoke it again.")
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