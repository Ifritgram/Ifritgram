from telethon import events
from os import remove
import modules.client
from PIL import Image, ImageFilter
from telethon.tl.functions.users import GetFullUserRequest

client = modules.client.client


@events.register(events.NewMessage(outgoing=True, pattern=r"\.ia"))
async def runia(event):
    await event.delete()
    selectoption = event.message.raw_text.split()
    messagelocation = event.to_id
    try:
        if selectoption[1] == "targetuser":
            try:
                getinformation = await event.get_reply_message()
                targetid = getinformation.sender_id
                targetdetails = await client(GetFullUserRequest(targetid))
                userdp = await client.download_profile_photo(
                    f"@{targetdetails.users[0].username}"
                )
                await client.send_file(messagelocation, userdp)
                remove(userdp)
            except:
                await event.client.send_message(
                    messagelocation, "Something Went Wrong"
                )
        elif selectoption[1] == "blur":
            targetcontent = await event.get_reply_message()
            picturename = "blurbyridogram.png"
            downloadtargetcontent = await event.client.download_media(
                targetcontent, picturename
            )
            bluramount = selectoption[2]
            try:
                targetimage = Image.open(downloadtargetcontent)
                blurredimage = targetimage.filter(
                    ImageFilter.GaussianBlur(int(bluramount))
                )
                blurredimage.save(picturename)
                send = await client.send_file(messagelocation, picturename)
                remove(picturename)
            except:
                await event.client.send_message(
                    messagelocation, "Something Went Wrong"
                )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
