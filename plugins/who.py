import core.client
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest

crowgram = core.client.crowgram

@events.register(events.NewMessage(outgoing=True, pattern=r"\>who"))
async def check_user_history(event):
    try:
        crowgram.parse_mode = "markdown"
        await event.edit("```Crowgram is collecting user records...```")
        get_information = await event.get_reply_message()
        target_id = get_information.sender_id
        get_user_details = await crowgram(GetFullUserRequest(target_id))
        first_name = get_user_details.users[0].first_name
        bot = "@SangMata_beta_bot"
        data_not_found = "No data available"
        limited = "Sorry"
        async with crowgram.conversation(bot) as start_conversation:
            await start_conversation.send_message(f"{target_id}")
            get_message = await start_conversation.get_response(timeout=2)
            message = get_message.text
            if data_not_found in message:
                await event.edit(f"No information was found for {first_name}")
                await crowgram.send_read_acknowledge(start_conversation.chat_id)
            elif limited in message:
                await event.edit("Sorry, you have used up your quota for today. Note that your quota refreshes daily at 00:00 UTC.")
                await crowgram.send_read_acknowledge(start_conversation.chat_id)
            else:
                await event.edit(f"User records found by Crowgram\n\n{message}")
                await crowgram.send_read_acknowledge(start_conversation.chat_id)
    except:
        pass