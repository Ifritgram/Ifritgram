from telethon import events
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest
import modules.client

client = modules.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r"\.kick"))
async def runkick(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    getmessage = await event.get_reply_message()
    targetuser = getmessage.sender_id
    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    getreason = event.message.raw_text.splitlines()
    replacecmd = getreason[0].replace(".kick ", "")
    kickedreason = replacecmd.splitlines()
    reason = kickedreason[0]
    client.parse_mode = "html"
    try:
        await event.client.kick_participant(
            messagelocation, getmessage.sender.id
        )
        if reason:
            if ".kick" in reason:
                await event.client.send_message(
                    messagelocation,
                    f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> Has Been Kicked",
                )
            else:
                await event.client.send_message(
                    messagelocation,
                    f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> Has Been Kicked\nReason: {reason}",
                )
        else:
            await event.client.send_message(
                messagelocation,
                f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> Has Been Kicked",
            )
    except:
        pass
