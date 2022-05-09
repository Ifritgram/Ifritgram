from telethon import events
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest
import modules.client

client = modules.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r"\.ban"))
async def runban(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    getmessage = await event.get_reply_message()
    targetuser = getmessage.sender_id
    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    client.parse_mode = "html"
    getreason = event.message.raw_text.splitlines()
    replacecmd = getreason[0].replace(".ban ", "")
    bannedreason = replacecmd.splitlines()
    reason = bannedreason[0]
    try:
        await event.client.edit_permissions(
            messagelocation, targetuser, view_messages=False
        )
        if reason:
            if ".ban" in reason:
                await event.client.send_message(
                    messagelocation,
                    f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> Has Been Banned",
                )
            else:
                await event.client.send_message(
                    messagelocation,
                    f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> Has Been Banned\nReason: {reason}",
                )
        else:
            await event.client.send_message(
                messagelocation,
                f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> Has Been Banned",
            )
    except ValueError:
        await event.client.send_message(
            messagelocation, "It's Not A Supergroup"
        )
    except:
        pass
