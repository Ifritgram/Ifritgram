from telethon import events
from asyncio import gather
import modules.client

client = modules.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r"\.rmf"))
async def runrmf(event):
    messagelocation = event.to_id
    messageslimit = event.message.raw_text.split()
    try:
        gather(
            *[
                client.delete_messages(messagelocation, id)
                for id in [
                    msg.id
                    for msg in await client.get_messages(
                        messagelocation, limit=int(messageslimit[1])
                    )
                    if msg
                ]
            ]
        )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
