from telethon import events
from PIL import Image
from time import sleep
from os import remove


@events.register(events.NewMessage(outgoing=True, pattern=r"\.itp"))
async def runitp(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    getcontent = await event.get_reply_message()
    messagelocation = event.to_id
    usercontent = "imageforpdf.png"
    filename = "pdfbyridogram.pdf"
    try:
        targetimage = await event.get_reply_message()
        downloadtargetimage = await event.client.download_media(
            targetimage, usercontent
        )
        opentargetimage = Image.open(usercontent)
        converttargetcontent = opentargetimage.convert("RGB")
        converttargetcontent.save(filename, "PDF", resolution=95)
        await event.client.send_file(messagelocation, filename)
        remove(usercontent)
        remove(filename)
    except:
        pass
