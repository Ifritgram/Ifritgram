from telethon import events
from asyncio import gather


@events.register(events.NewMessage(outgoing=True, pattern=r"\.ar"))
async def runar(event):
    await event.delete()
    messagelocation = event.to_id
    reactinformation = event.message.raw_text.split()
    try:
        gather(
            *[
                await event.client.send_reaction(
                    messagelocation, id, f"{reactinformation[3]}"
                )
                for id in [
                    msg.id
                    for msg in await event.client.get_messages(
                        messagelocation,
                        limit=int(reactinformation[2]),
                        from_user=reactinformation[1],
                    )
                    if msg
                ]
            ]
        )
    except:
        pass
