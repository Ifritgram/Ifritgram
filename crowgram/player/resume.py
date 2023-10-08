import core.client
from os import environ
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from pytgcalls.exceptions import GroupCallNotFound

crowgram_assistant = core.client.crowgram_assistant
call = core.client.crowgram_call
owner = int(environ["owner"])

@events.register(events.NewMessage(incoming=True, pattern=r"\>resume"))
async def resume_audio(event):
    try:
        await event.delete()
    except:
        pass
    chat_id = event.to_id.channel_id
    requestor_id = event.from_id.user_id
    get_user_details = await crowgram_assistant(GetFullUserRequest(requestor_id))
    first_name = get_user_details.users[0].first_name
    crowgram_assistant.parse_mode = "html"
    if owner == requestor_id:
        try:
            await call.resume_stream(chat_id)
            await crowgram_assistant.send_message(chat_id, f"⏸ Resumed\n👤Order by: <a href='tg://user?id={requestor_id}'>{first_name}</a>")
        except GroupCallNotFound:
            await crowgram_assistant.send_message(chat_id, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️Cannot resume because streaming is not running.")
        except:
            pass
    else:
        await crowgram_assistant.send_message(chat_id, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️You don't have permission to use me; please deploy your own Crowgram.")