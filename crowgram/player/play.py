import core.client
from os import environ, remove
from telethon import events
from youtubesearchpython import VideosSearch
from telethon.tl.functions.users import GetFullUserRequest
import yt_dlp
from pytgcalls.types import AudioPiped
from pytgcalls.exceptions import NoActiveGroupCall, AlreadyJoinedError
from pytgcalls.types import Update

crowgram_assistant = core.client.crowgram_assistant
call = core.client.crowgram_call
owner = int(environ["owner"])

@events.register(events.NewMessage(incoming=True, pattern=r"\>play"))
async def play_audio(event):
    try:
        await event.delete()
    except:
        pass
    message_location = event.to_id.channel_id
    requestor_id = event.from_id.user_id
    get_data = event.message.raw_text.splitlines()
    command = ">play"
    remove_command = get_data[0].replace(">play ", "")
    get_song_name = remove_command.splitlines()
    song_name = get_song_name[0]
    get_user_details = await crowgram_assistant(GetFullUserRequest(requestor_id))
    first_name = get_user_details.users[0].first_name
    crowgram_assistant.parse_mode = "html"
    if owner == requestor_id:
        if command in get_song_name:
            await crowgram_assistant.send_message(message_location, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️No song name was found; please enter a song name.")
        else:
            def get_seconds(time_str):
                minutes, seconds = time_str.split(":")
                return int(minutes) * 60           
            videosSearch = VideosSearch(song_name, limit = 1)
            song_title = videosSearch.result()["result"][0]["title"]
            song_link = videosSearch.result()["result"][0]["link"]
            song_duration = videosSearch.result()["result"][0]["duration"]
            get_duration = get_seconds(song_duration)
            song_duration_limit = 600
            if get_duration > song_duration_limit:
                await crowgram_assistant.send_message(message_location, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️Only songs with a duration of less than 10 minutes are acceptable.")
            else:
                ydl_opts = {
                    "format": "mp3/bestaudio/best",
                    "postprocessors": [
                        {
                            "key": "FFmpegExtractAudio",
                            "preferredcodec": "mp3"
                        }
                    ],
                    "outtmpl": "song"
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(song_link)              
                try:
                    await call.join_group_call(message_location, AudioPiped("song.mp3"))
                    remove("song.mp3")
                    await crowgram_assistant.send_message(message_location, f"🔉 Streaming has started\n\n🎧 Name: {song_title}\n⌛️ Duration: {song_duration}\n👤 Requested By: <a href='tg://user?id={requestor_id}'>{first_name}</a>\n🔗 Source: <a href='{song_link}'>Click Here</a>", link_preview=False)
                except NoActiveGroupCall:
                    remove("song.mp3")
                    await crowgram_assistant.send_message(message_location, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️Group Call is not running; please start Group Call first.")
                except AlreadyJoinedError:
                    remove("song.mp3")
                    await crowgram_assistant.send_message(message_location, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️Already streaming is in progress; please wait until it finishes.")
                except:
                    pass
    else:
        await crowgram_assistant.send_message(message_location, f"Dear <a href='tg://user?id={requestor_id}'>{first_name}</a>,\n❗️You don't have permission to use me; please deploy your own Crowgram.")

@call.on_stream_end()
async def stream_end_handler(_, u: Update):
    try:
        chat_id = u.chat_id
        await call.leave_group_call(chat_id)
    except:
        pass