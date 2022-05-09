from telethon import events
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
from time import sleep
from os import remove


@events.register(events.NewMessage(outgoing=True, pattern=r"\.qrc"))
async def runqrc(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    selectoption = event.message.raw_text.split()
    getuserdata = await event.get_reply_message()
    messagelocation = event.to_id
    filename = "qrcodecreatebyridogram.png"
    qrcodename = "qrcodeforscan.png"
    try:
        if selectoption[1] == "create":
            createqrcode = qrcode.make(f"{getuserdata.message}")
            createqrcode.save(filename)
            await event.client.send_file(messagelocation, filename)
            remove(filename)
        elif selectoption[1] == "scan":
            targetqrcode = await event.get_reply_message()
            downloadqrcode = await event.client.download_media(
                targetqrcode, qrcodename
            )
            qrcodedecoder = decode(Image.open(qrcodename))
            await event.client.send_message(
                messagelocation,
                f"QR Code Data: {qrcodedecoder[0].data.decode()}",
            )
            remove(qrcodename)
        else:
            await event.client.send_message(messagelocation, "Wrong Option")
    except IndexError:
        await event.client.send_message(messagelocation, "Select An Option")
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
