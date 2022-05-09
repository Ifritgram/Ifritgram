from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
import os


@events.register(events.NewMessage)
async def runpmlog(event):
    try:
        pmlog_location = int(os.environ["pmlog_location"])
        getridogramuserdetails = await event.client(GetFullUserRequest("me"))
        ridogramuser = getridogramuserdetails.users[0].id
        user = await event.get_chat()
        senderinformation = await event.client(GetFullUserRequest(user.id))
        itisbot = senderinformation.users[0].bot
        isridogramuser = await event.get_sender()
        if pmlog_location:
            if event.is_private:
                if itisbot == True:
                    pass
                else:
                    if user.id == ridogramuser:
                        pass
                    else:
                        if ridogramuser == isridogramuser.id:
                            pass
                        else:
                            userdata = event.message
                            await event.client.forward_messages(
                                pmlog_location, userdata
                            )
        else:
            pass
    except:
        pass


@events.register(events.NewMessage)
async def runmentionlog(event):
    try:
        mentionlog_location = int(os.environ["mentionlog_location"])
        checkmention = event.mentioned
        update = await event.get_chat()
        if mentionlog_location:
            if checkmention == True:
                mentiondata = event.message.message
                fromthisid = event.from_id.user_id
                fetchinfo = await event.client(GetFullUserRequest(fromthisid))
                fromthisuser = fetchinfo.users[0].first_name
                await event.client.send_message(
                    mentionlog_location,
                    f"From: {update.title}\nUser: {fromthisuser}\nMessage: {mentiondata}",
                )
        else:
            pass
    except:
        pass
