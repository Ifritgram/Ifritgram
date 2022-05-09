from telethon import events


@events.register(events.NewMessage(outgoing=True, pattern=r"\.q"))
async def runq(event):
    messagelocation = event.to_id
    repliedmessage = await event.get_reply_message()
    await event.edit("Processing...")
    targetbot = "QuotLyBot"
    try:
        working = await repliedmessage.forward_to(targetbot)
        async with event.client.conversation(targetbot) as startconversation:
            message = await startconversation.get_response(working.id)
            await event.client.send_read_acknowledge(startconversation.chat_id)
            await event.client.send_message(messagelocation, message)
            await event.delete()
    except:
        pass
