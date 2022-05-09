from telethon import events
from async_timeout import asyncio


@events.register(events.NewMessage(outgoing=True, pattern=r"\.uh"))
async def runuh(event):
    await event.edit("Ridogram Collect User Records...")
    getinformation = await event.get_reply_message()
    targetid = getinformation.sender_id
    bot = "@SangMataInfo_bot"
    async with event.client.conversation(bot) as startconversation:
        await startconversation.send_message(f"/search_id {targetid}")
        infobotresponse = []
        while True:
            try:
                message = await startconversation.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            infobotresponse.append(message.text)
        datalenght = len(infobotresponse)
        try:
            if "No records found" in infobotresponse:
                await event.edit("User Record Not Found")
            else:
                if datalenght == 3:
                    if "🔗 Link To Profile" in infobotresponse:
                        infobotresponse.remove("🔗 Link To Profile")
                        await event.edit(
                            f"{infobotresponse[0]}\n\n{infobotresponse[1]}"
                        )
                    elif (
                        f"🔗 [Link To Profile](tg://user?id={targetid})"
                        in infobotresponse
                    ):
                        infobotresponse.remove(
                            f"🔗 [Link To Profile](tg://user?id={targetid})"
                        )
                        await event.edit(
                            f"{infobotresponse[0]}\n\n{infobotresponse[1]}"
                        )
                elif datalenght == 2:
                    if "🔗 Link To Profile" in infobotresponse:
                        infobotresponse.remove("🔗 Link To Profile")
                        await event.edit(f"{infobotresponse[0]}")
                    elif (
                        f"🔗 [Link To Profile](tg://user?id={targetid})"
                        in infobotresponse
                    ):
                        infobotresponse.remove(
                            f"🔗 [Link To Profile](tg://user?id={targetid})"
                        )
                        await event.edit(f"{infobotresponse[0]}")
                elif datalenght == 1:
                    if "🔗 Link To Profile" in infobotresponse:
                        infobotresponse.remove("🔗 Link To Profile")
                        await event.edit("User Record Not Found")
                    elif (
                        f"🔗 [Link To Profile](tg://user?id={targetid})"
                        in infobotresponse
                    ):
                        infobotresponse.remove(
                            f"🔗 [Link To Profile](tg://user?id={targetid})"
                        )
                        await event.edit("User Record Not Found")
                    else:
                        await event.edit(f"{infobotresponse[0]}")
        except:
            pass
