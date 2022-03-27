from telethon import events
import base64
from time import sleep

@events.register(events.NewMessage(outgoing=True, pattern=r'\.b64'))
async def runb64(event):
    await event.edit("Processing...")
    options = event.message.raw_text.split()
    selectsecretmessage = await event.get_reply_message()
    try:
        if options[1] == "en":
            secretmessage = selectsecretmessage.message
            secretmessagebytes = secretmessage.encode("ascii")
            encodesecretmessage = base64.b64encode(secretmessagebytes)
            encodesecretmessagebytes = encodesecretmessage.decode("ascii")
            await event.edit("Encrypting...")
            sleep(2)
            await event.edit(f"{encodesecretmessagebytes}")
        elif options[1] == "de":
            secretkey = selectsecretmessage.message
            secretkeybytes = secretkey.encode("ascii")
            decodesecretkey = base64.b64decode(secretkeybytes)
            decodesecretkeybytes = decodesecretkey.decode("ascii")
            await event.edit("Decrypting...")
            sleep(2)
            await event.edit(f"Decrypted Message: {decodesecretkeybytes}")
        else:
            await event.edit("Wrong Option")
    except IndexError:
        await event.edit("Select An Option")
    except:
        await event.edit("Something Went Wrong") 