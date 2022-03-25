from telethon import events
from time import sleep
from async_timeout import asyncio

@events.register(events.NewMessage(outgoing=True, pattern=r'\.uh'))
async def runuh(event):
    await event.edit("Ridogram Collect User Records...")
    sleep(2)
    getinformation = await event.get_reply_message()
    targetid = getinformation.sender_id
    bot = "@SangMataInfo_bot"
    async with event.client.conversation(bot) as startconversation:
        await startconversation.send_message(f"/search_id {targetid}")
        infobotresponse= []
        while True:
            try:
                message = await startconversation.get_response(timeout=2)
            except asyncio.TimeoutError:
               break
            infobotresponse.append(message.text)
        try:
            if "No records found" in infobotresponse:
                await event.edit("User Record Not Found")
            else:
                await event.edit(f"{infobotresponse[0]}\n\n{infobotresponse[1]}\n\n{infobotresponse[2]}")
        except:
            pass