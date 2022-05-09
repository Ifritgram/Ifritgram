from telethon import events
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest
from telethon import functions

approvedusers = set([])
protectionmode = set([])


@events.register(events.NewMessage(outgoing=True, pattern=r"\.guardon"))
async def runpmgmon(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        if protectionmode:
            if "off" in protectionmode:
                protectionmode.remove("off")
        guardmodeon = "on"
        if guardmodeon in protectionmode:
            await event.client.send_message(
                messagelocation, "PM Protection Already Activated"
            )
        else:
            protectionmode.add(guardmodeon)
            await event.client.send_message(
                messagelocation, "PM Protection Successfully Activated"
            )
    except:
        pass


@events.register(events.NewMessage(outgoing=True, pattern=r"\.guardoff"))
async def runpmgmoff(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        guardmodeoff = "off"
        if "on" in protectionmode:
            protectionmode.remove("on")
        if guardmodeoff in protectionmode:
            await event.client.send_message(
                messagelocation, "PM Protection Already Deactivated"
            )
        else:
            protectionmode.add(guardmodeoff)
            await event.client.send_message(
                messagelocation, "PM Protection Successfully Deactivated"
            )
    except:
        pass


@events.register(events.NewMessage(outgoing=True, pattern=r"\.guardstatus"))
async def runpmgmstatus(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        statusinformation = []
        if protectionmode:
            for details in protectionmode:
                statusinformation.append(details)
            convertdata = "\n".join(statusinformation)
            await event.client.send_message(
                messagelocation, f"Guard Status: {convertdata.title()}"
            )
        else:
            await event.client.send_message(
                messagelocation, "PM Protection Is Off By Default"
            )
    except:
        pass


@events.register(events.NewMessage(outgoing=True, pattern=r"\.pa"))
async def runap(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        getinformation = await event.get_reply_message()
        selecteduser = getinformation.sender_id
        if selecteduser not in approvedusers:
            approvedusers.add(selecteduser)
            await event.client.send_message(
                messagelocation, "This User Has Been Successfully Approved"
            )
        else:
            await event.client.send_message(
                messagelocation, "This User Is Already Approved"
            )
    except:
        pass


@events.register(events.NewMessage(outgoing=True, pattern=r"\.pda"))
async def rununap(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        getinformation = await event.get_reply_message()
        selecteduser = getinformation.sender_id
        if selecteduser in approvedusers:
            approvedusers.remove(selecteduser)
            await event.client.send_message(
                messagelocation,
                "This User Has Been Successfully Removed From The Approved List",
            )
        else:
            await event.client.send_message(
                messagelocation, "This User Is Not Already Approved"
            )
    except:
        pass


@events.register(
    events.NewMessage(outgoing=True, pattern=r"\.showapprovedlist")
)
async def runpmapprovedlist(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        approveddetails = []
        if approvedusers:
            for details in approvedusers:
                approveddetails.append(details)
            convertdata = "\n".join(map(str, approveddetails))
            lenght = len(approvedusers)
            if lenght == 1:
                await event.client.send_message(
                    messagelocation, f"Approved User:\n{convertdata}"
                )
            else:
                await event.client.send_message(
                    messagelocation, f"Approved Users:\n{convertdata}"
                )
        else:
            await event.client.send_message(
                messagelocation, "Approved User Not Found"
            )
    except:
        pass


@events.register(events.NewMessage)
async def runpmguard(event):
    if event.is_private:
        getridogramuserdetails = await event.client(GetFullUserRequest("me"))
        ridogramuser = getridogramuserdetails.users[0].id
        user = await event.get_chat()
        messagelocation = user.id
        blockimage = "http://telegra.ph/file/044cdfc719b352c7eb5e0.png"
        senderinformation = await event.client(GetFullUserRequest(user.id))
        itisbot = senderinformation.users[0].bot
        isridogramuser = await event.get_sender()
        try:
            if "on" in protectionmode:
                if itisbot == True:
                    pass
                else:
                    if user.id not in approvedusers:
                        if user.id == ridogramuser:
                            pass
                        else:
                            if ridogramuser == isridogramuser.id:
                                pass
                            else:
                                await event.client.send_file(
                                    messagelocation,
                                    blockimage,
                                    caption=f"Dear {user.first_name},\nThank you for sending me a message but I'm blocking you temporarily because I'm not allowing you to send me a message so please wait for my permission.",
                                )
                                await event.client(
                                    functions.contacts.BlockRequest(user.id)
                                )
        except:
            pass
