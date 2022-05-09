from telethon import events
from time import sleep
from usernames import is_safe_username


@events.register(events.NewMessage(outgoing=True, pattern=r"\.uv"))
async def runuv(event):
    await event.edit("Checking...")
    sleep(2)
    await event.delete()
    getusername = await event.get_reply_message()
    messagelocation = event.to_id
    try:
        scanreport = is_safe_username(f"{getusername.message}")
        if scanreport == True:
            await event.client.send_message(
                messagelocation,
                f"Good News, {getusername.message} Was Not Found On Ridogram Blacklist.",
            )
        elif scanreport == False:
            await event.client.send_message(
                messagelocation,
                f"{getusername.message} Was Found On Ridogram Blacklist.",
            )
        else:
            await event.client.send_message(
                messagelocation, "Something Went Wrong"
            )
    except:
        pass
