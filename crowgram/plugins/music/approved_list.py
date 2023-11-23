'''
Plugin Name: Approved List
Developer: iniridwanul
License: AGPL-3.0 license
'''

import core.client
from os import environ
from telethon import events
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import BlockRequest

crowgram_assistant = core.client.crowgram_assistant
owner = int(environ["owner"])

@events.register(events.NewMessage(incoming=True, pattern=r"\>l"))
async def show_approved_list(event):
    try:
        if event.is_private:
            commander = event.original_update.user_id
            if commander == owner:
                await event.delete()
                users_name = set([])
                contacts = await crowgram_assistant(GetContactsRequest(hash=0))
                for user_details in contacts.users:
                    get_details = await crowgram_assistant(GetFullUserRequest(user_details.id))
                    first_name = get_details.users[0].first_name
                    users_name.add(f"👤 {first_name}")
                name = "\n".join(users_name)
                await crowgram_assistant.send_message(commander, f"List of people allowed to play music:\n\n{name}")
            else:
                crowgram_image = "https://telegra.ph/file/700b7f318d380cb2d228d.jpg"
                await crowgram_assistant.send_file(commander, crowgram_image, caption="You are not allowed to use this powerful command, yet you tried to do malicious activities using this command, so you were blocked by the automatic system.\n\nThanks,\n@Crowgram")
                await crowgram_assistant(BlockRequest(commander))
    except:
        pass