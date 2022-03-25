from telethon import events
import modules.client
from telethon.tl.functions.users import GetFullUserRequest
from os import remove

client = modules.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.dls'))
async def rundls(event):
    await event.delete()
    getinformation = await event.get_reply_message()
    targetid = getinformation.sender_id
    targetdetails = await client(GetFullUserRequest(targetid))
    messagelocation = event.to_id
    client.parse_mode = "html"
    userimage = await client.download_profile_photo(f"@{targetdetails.user.username}")
    try:
        await client.send_file(messagelocation, userimage, caption=f"Firstname: {targetdetails.user.first_name}\nLastname: {targetdetails.user.last_name}\nUsername: @{targetdetails.user.username}\nUser ID: {targetdetails.user.id}\nPhone Number: {targetdetails.user.phone}\nUser Link: <a href='tg://user?id={targetid}'>Profile</a>\nBio: {targetdetails.about}\nData Center ID: {targetdetails.user.photo.dc_id}\nBot: {targetdetails.user.bot}\nContact: {targetdetails.user.contact}\nBlock Contact: {targetdetails.blocked}\nMutual Groups: {targetdetails.common_chats_count}")
        remove(userimage)
    except:
        pass