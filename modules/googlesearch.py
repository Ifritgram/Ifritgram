from telethon import events
from time import sleep
from googlesearch import search


@events.register(events.NewMessage(outgoing=True, pattern=r"\.gs"))
async def rungs(event):
    await event.edit("Searching...")
    sleep(2)
    await event.delete()
    getquery = event.message.raw_text.splitlines()
    replacedata = getquery[0].replace(".gs ", "")
    mainquery = replacedata.splitlines()
    allresults = []
    messagelocation = event.to_id
    try:
        for results in search(mainquery[0], num_results=10):
            allresults.append(results)
        getgoogledata = "\n\n".join(allresults)
        await event.client.send_message(messagelocation, f"{getgoogledata}")
    except:
        pass
