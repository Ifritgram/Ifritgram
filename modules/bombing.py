from telethon import events
import modules.client

client = modules.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r"\.bomb"))
async def runbomb(event):
    await event.delete()
    default = 0
    need = event.message.raw_text.splitlines()
    replaceone = need[0].replace(".bomb ", "")
    createlist = replaceone.split()
    createlist.pop(0)
    joincontent = " ".join(createlist)
    maincontent = joincontent.splitlines()
    againneed = event.message.raw_text.split()
    bombmessagelocation = event.to_id
    while default < int(againneed[1]):
        await client.send_message(bombmessagelocation, f"{maincontent[0]}")
        default += 1
