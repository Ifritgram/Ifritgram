from telethon import events
from datetime import datetime
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest

afkmode = set([])

@events.register(events.NewMessage(outgoing=True, pattern=r'\.afkon'))
async def runafkon(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        if afkmode:
            if "off" in afkmode:
                afkmode.remove("off")
        afkmodeon = "on"
        if afkmodeon in afkmode:
            await event.client.send_message(messagelocation, "AFK Mode Already Activated")
        else:
            afkmode.add(afkmodeon)
            runafkon.start = datetime.now()
            await event.client.send_message(messagelocation, "AFK Mode Successfully Activated")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.afkoff'))
async def runafkoff(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        afkmodeoff = "off"
        if "on" in afkmode:
            afkmode.remove("on")
        if afkmodeoff in afkmode:
            await event.client.send_message(messagelocation, "AFK Mode Already Deactivated")
        else:
            afkmode.add(afkmodeoff)
            await event.client.send_message(messagelocation, "AFK Mode Successfully Deactivated")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.afkstatus'))
async def runafkstatus(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        statusinformation = []
        if afkmode:
            for details in afkmode:
                statusinformation.append(details)
            convertdata = "\n".join(statusinformation)
            await event.client.send_message(messagelocation, f"AFK Status: {convertdata.title()}")
        else:
            await event.client.send_message(messagelocation, "AFK Mode Is Off By Default")
    except:
        pass

@events.register(events.NewMessage)
async def runafk(event):
    if event.is_private:
        getridogramuserdetails = await event.client(GetFullUserRequest("me"))
        ridogramuser = getridogramuserdetails.users[0].id
        user = await event.get_chat()
        messagelocation = user.id
        senderinformation = await event.client(GetFullUserRequest(user.id))
        itisbot = senderinformation.users[0].bot
        isridogramuser = await event.get_sender()
        afkimage = "https://telegra.ph/file/bc206d17d44613507f5a6.png"
        try:
            if "on" in afkmode:
                if itisbot == True:
                    pass
                else:
                    if user.id == ridogramuser:
                        pass
                    else:
                        if ridogramuser == isridogramuser.id:
                            pass
                        else:
                            end = datetime.now()
                            total = (end - runafkon.start)
                            countthetime = int(total.seconds)
                            sd = countthetime // (24 * 3600)
                            countthetime %= 24 * 3600
                            sh = countthetime // 3600
                            countthetime %= 3600
                            sm = countthetime // 60
                            countthetime %= 60
                            ss = countthetime
                            endtime = ""
                            if sd > 0:
                                endtime += f"{sd}d {sh}h {sm}m {ss}s"
                            elif sh > 0:
                                endtime += f"{sh}h {sm}m {ss}s"
                            else:
                                endtime += f"{sm}m {ss}s" if sm > 0 else f"{ss}s"
                            await event.client.send_file(messagelocation, afkimage, caption=f"Dear {user.first_name},\nI'm sorry, I can't come to the computer right now, please leave a message.\n\nLast Seen: {endtime}")
        except:
            pass