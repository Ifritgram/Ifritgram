from telethon import events
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest
import modules.client

client = modules.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r"\.unban"))
async def rununban(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    getmessage = await event.get_reply_message()
    targetuser = getmessage.sender_id
    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    client.parse_mode = "html"
    try:
        await event.client.edit_permissions(
            messagelocation, targetuser, view_messages=True
        )
        await event.client.send_message(
            messagelocation,
            f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> Has Been Successfully Unbanned",
        )
    except ValueError:
        await event.client.send_message(
            messagelocation, "It's Not A Supergroup"
        )
    except:
        pass
