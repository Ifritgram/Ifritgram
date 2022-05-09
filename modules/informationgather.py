from telethon import events
from time import sleep
from telethon import functions


@events.register(events.NewMessage(outgoing=True, pattern=r"\.ig"))
async def runig(event):
    await event.edit("Checking...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    getusername = event.message.raw_text.split()
    validationusername = getusername[1].replace("@", "")
    try:
        targetgroup = await event.client(
            functions.channels.GetFullChannelRequest(f"{validationusername}")
        )
        informations = targetgroup.full_chat
        groupusername = f"@{validationusername}"
        groupid = informations.id
        groupdescription = informations.about
        groupdc = informations.chat_photo.dc_id
        members = informations.participants_count
        online = informations.online_count
        messageslowmode = informations.slowmode_seconds
        reactionsdata = informations.available_reactions
        availablereactions = " ".join(reactionsdata)
        await event.client.send_message(
            messagelocation,
            f"🔗 Username: {groupusername}\n\n🆔 ID: {groupid}\n\n📝 Description: {groupdescription}\n\n🌐 Data Center ID: {groupdc}\n\n👥 Total Members: {members}\n\n🟢 Online Users: {online}\n\n⏳ Slow Mode: {messageslowmode} Seconds\n\n🎭 Available Reactions: {availablereactions}",
        )
    except:
        pass
