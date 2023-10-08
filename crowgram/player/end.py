import core.client
from os import environ
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from pytgcalls.exceptions import NoActiveGroupCall, NotInGroupCallError

crowgram_assistant = core.client.crowgram_assistant
call = core.client.crowgram_call
owner = int(environ["owner"])

@events.register(events.NewMessage(incoming=True, pattern=r"\>end"))
async def end_audio(event):
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
            await call.leave_group_call(chat_id)
            await crowgram_assistant.send_message(chat_id, f"🔇 Streaming has ended\n👤 Order by: <a href='tg://user?id={requestor_id}'>{first_name}</a>")
        except NoActiveGroupCall:
            await crowgram_assistant.send_message(chat_id, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️Streaming is not on, so streaming is already off.")
        except NotInGroupCallError:
            await crowgram_assistant.send_message(chat_id, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️Streaming is not on, so streaming is already off.")
        except:
            pass
    else:
        await crowgram_assistant.send_message(chat_id, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️You don't have permission to use me; please deploy your own Crowgram.")