from telethon import events


@events.register(events.NewMessage(outgoing=True, pattern=r"\.fag"))
async def runfag(event):
    await event.edit("Processing...")
    getgroupname = []
    getgroupusername = []
    getgroupid = []
    messagelocation = event.to_id
    try:
        async for getgroup in event.client.iter_dialogs():
            if getgroup.is_group:
                getgroupname.append(f"👥 {getgroup.name}")
                getgroupusername.append(f"📎 @{getgroup.entity.username}")
                getgroupid.append(str(f"🆔 {getgroup.id}"))
        convertname = "\n".join(getgroupname)
        convertusername = "\n".join(getgroupusername)
        convertid = "\n".join(getgroupid)
        await event.delete()
        await event.client.send_message(
            messagelocation,
            f"Group Name:\n{convertname}\n\nGroup Username:\n{convertusername}\n\nGroup ID:\n{convertid}",
        )
    except:
        pass


@events.register(events.NewMessage(outgoing=True, pattern=r"\.id"))
async def runfcid(event):
    await event.delete()
    try:
        fetchchatid = event.chat_id
        messagelocation = event.to_id
        await event.client.send_message(
            messagelocation, f"This Chat's ID Is: {fetchchatid}"
        )
    except:
        pass
