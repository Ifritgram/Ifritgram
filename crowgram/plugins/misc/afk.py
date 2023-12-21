'''
Plugin Name: AFK (Away From Keyboard)
Developer: iniridwanul
License: AGPL-3.0 license
'''

import core.client
from telethon import events
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest

crowgram = core.client.crowgram
afk_mode = set([])

@events.register(events.NewMessage(outgoing=True, pattern=r"\>onafk"))
async def activate_afk_mode(event):
    try:
        crowgram.parse_mode = "markdown"
        await event.edit("```Processing...```")
        sleep(2)
        await event.delete()
        message_location = event.to_id
        get_reason = event.message.raw_text.splitlines()
        remove_cmd = get_reason[0].replace(">onafk ", "")
        activate_afk_mode.afk_reason = remove_cmd.splitlines()
        activate_afk_mode.reason = activate_afk_mode.afk_reason[0]
        if not afk_mode:
            afk_mode.add("on")
            await crowgram.send_message(message_location, "AFK Mode has been successfully activated.")
        else:
            if "off" in afk_mode:
                afk_mode.remove("off")
                afk_mode.add("on")
                await crowgram.send_message(message_location, "AFK Mode has been successfully activated.")
            elif "on" in afk_mode:
                await crowgram.send_message(message_location, "AFK mode is already activated; if any data has been changed, then it has been successfully updated.")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r"\>offafk"))
async def deactivate_afk_mode(event):
    try:
        crowgram.parse_mode = "markdown"
        await event.edit("```Processing...```")
        sleep(2)
        await event.delete()
        message_location = event.to_id
        if "on" in afk_mode:
            afk_mode.remove("on")
            afk_mode.add("off")
            await crowgram.send_message(message_location, "AFK mode has been successfully deactivated.")
        elif "off" in afk_mode:
            await crowgram.send_message(message_location, "AFK Mode has already been deactivated.")
        else:
            await crowgram.send_message(message_location, "AFK mode is deactivated by default.")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r"\>checkafk"))
async def check_afk_status(event):
    try:
        crowgram.parse_mode = "markdown"
        await event.edit("```Processing...```")
        sleep(2)
        await event.delete()
        message_location = event.to_id
        if afk_mode:
            afk_status = []
            for afk_information in afk_mode:
                afk_status.append(afk_information)
            mode = afk_status[0].title()
            await crowgram.send_message(message_location, f"AFK Status: {mode}")
        else:
            await crowgram.send_message(message_location, "AFK mode is deactivated by default.")
    except:
        pass

@events.register(events.NewMessage)
async def afk_notification(event):
    try:
        if "on" in afk_mode:
            cmd = ">onafk"
            reply_location = event.id
            if event.is_private:
                user = event.peer_id.user_id     
                find_crowgram_user = await crowgram(GetFullUserRequest("me"))
                crowgram_user = find_crowgram_user.users[0].id
                get_sender = await event.get_sender()
                sender = get_sender.id
                sender_type = await event.get_chat()
                bot = sender_type.bot
                telegram = 777000
                if user == crowgram_user:
                    pass
                elif sender == crowgram_user:
                    pass
                elif user == telegram:
                    pass
                elif bot:
                    pass
                else:
                    if activate_afk_mode.reason:
                        if cmd in activate_afk_mode.reason:
                            await crowgram.send_message(user, f"Dear {sender_type.first_name},\nI'm sorry, I can't come to the computer right now. Please wait for me. For your information, this is an automated message from Crowgram.\n\nThank You", reply_to=reply_location)
                        else:
                            await crowgram.send_message(user, f"Dear {sender_type.first_name},\nI'm sorry, I can't come to the computer right now. Please wait for me. For your information, this is an automated message from Crowgram.\n\nAFK Reason: {activate_afk_mode.reason}\n\nThank You", reply_to=reply_location)
                    else:
                        await crowgram.send_message(user, f"Dear {sender_type.first_name},\nI'm sorry, I can't come to the computer right now. Please wait for me. For your information, this is an automated message from Crowgram.\n\nThank You", reply_to=reply_location)
            elif event.mentioned:
                mentioned_location = event.to_id
                user_id = event.from_id.user_id
                get_user_details = await crowgram(GetFullUserRequest(user_id))
                first_name = get_user_details.users[0].first_name
                if activate_afk_mode.reason:
                    if cmd in activate_afk_mode.reason:
                        await crowgram.send_message(mentioned_location, f"Dear {first_name},\nI'm sorry, I can't come to the computer right now. Please wait for me. For your information, this is an automated message from Crowgram.\n\nThank You", reply_to=reply_location)
                    else:
                        await crowgram.send_message(mentioned_location, f"Dear {first_name},\nI'm sorry, I can't come to the computer right now. Please wait for me. For your information, this is an automated message from Crowgram.\n\nAFK Reason: {activate_afk_mode.reason}\n\nThank You", reply_to=reply_location)
                else:
                    await crowgram.send_message(mentioned_location, f"Dear {first_name},\nI'm sorry, I can't come to the computer right now. Please wait for me. For your information, this is an automated message from Crowgram.\n\nThank You", reply_to=reply_location)         
    except:
        pass