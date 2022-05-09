from telethon import events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from os import remove


@events.register(events.NewMessage(outgoing=True, pattern=r"\.uau"))
async def runuau(event):
    await event.edit("Updating...")
    selectoption = event.message.raw_text.split()
    getupdate = await event.get_reply_message()
    targetcontent = await event.get_reply_message()
    downloadtargetcontent = await targetcontent.download_media()
    try:
        if selectoption[1] == "nc":
            await event.client(
                UpdateProfileRequest(first_name=f"{getupdate.message}")
            )
            await event.edit("Name Changed")
        elif selectoption[1] == "bc":
            await event.client(
                UpdateProfileRequest(about=f"{getupdate.message}")
            )
            await event.edit("Bio Changed")
        elif selectoption[1] == "uc":
            await event.client(UpdateUsernameRequest(f"{getupdate.message}"))
            await event.edit("Username Changed")
        elif selectoption[1] == "ppc":
            await event.client(
                UploadProfilePhotoRequest(
                    await event.client.upload_file(f"{downloadtargetcontent}")
                )
            )
            await event.edit("Profile Picture Changed")
            remove(downloadtargetcontent)
    except:
        pass
