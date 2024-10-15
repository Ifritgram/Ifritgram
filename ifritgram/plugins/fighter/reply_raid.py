import core.client
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from os import environ
from random import choice
from docsdata import slangs

ifritgram = core.client.ifritgram
opponent = set([])
owner = int(environ["owner"])

@events.register(events.NewMessage(outgoing=True, pattern=r"\>so"))
async def find_opponent(event):
    try:
        await event.delete()
        find_user = await event.get_reply_message()
        user_id = find_user.sender_id
        chat = event.to_id
        message = await event.get_reply_message()
        reply = message.id
        get_first_name = await ifritgram(GetFullUserRequest(user_id))
        first_name = get_first_name.users[0].first_name
        if user_id not in opponent:
            opponent.add(user_id)
            ifritgram.parse_mode = "html"
            await ifritgram.send_message(chat, f"<a href='tg://user?id={user_id}'>{first_name}</a> You are imprisoned in the eyes of Ifritgram. From now on, your forehead will start writing.", reply_to=reply)
        else:
            await ifritgram.send_message(chat, f"<a href='tg://user?id={user_id}'>{first_name}</a> This user has already been locked up in Ifritgram's jail.", reply_to=reply)
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r"\>ro"))
async def remove_opponent(event):
    await event.delete()
    find_user = await event.get_reply_message()
    user_id = find_user.sender_id
    chat = event.to_id
    message = await event.get_reply_message()
    reply = message.id
    get_first_name = await ifritgram(GetFullUserRequest(user_id))
    first_name = get_first_name.users[0].first_name
    if user_id in opponent:
        opponent.remove(user_id)
        ifritgram.parse_mode = "html"
        await ifritgram.send_message(chat, f"<a href='tg://user?id={user_id}'>{first_name}</a> Given a chance to start a new life, freed from Ifritgram's gaze.", reply_to=reply)
    else:
        await ifritgram.send_message(chat, f"<a href='tg://user?id={user_id}'>{first_name}</a> This user has already been released from Ifritgram jail.", reply_to=reply)

@events.register(events.NewMessage)
async def chat_fight(event):
    if event.is_private:
        user_id = event.peer_id.user_id
        sender = await event.get_sender()
        sender_id = sender.id
        reply = event.id
        if opponent:
            if user_id in opponent:
                if sender_id == owner:
                    pass
                else:
                    get_first_name = await ifritgram(GetFullUserRequest(user_id))
                    first_name = get_first_name.users[0].first_name
                    ifritgram.parse_mode = "html"
                    random_hindi_slangs = choice(slangs.hindi_slangs)
                    await ifritgram.send_message(user_id, f"<a href='tg://user?id={user_id}'>{first_name}</a> {random_hindi_slangs}", reply_to=reply)