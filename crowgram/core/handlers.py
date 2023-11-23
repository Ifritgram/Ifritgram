import core.client
import os
from plugins import misc, music
import utils
from telethon import sync
from telethon import version
from platform import python_version
from pytgcalls import __version__

crowgram = core.client.crowgram
crowgram_bot = core.client.crowgram_bot
crowgram_assistant = core.client.crowgram_assistant
log_group = int(os.environ["log_group"])

def run_handlers():
    with crowgram as crowgram_ai:
        crowgram_ai.add_event_handler(misc.check_alive)
        crowgram_ai.add_event_handler(misc.pinged)
        crowgram_ai.add_event_handler(misc.get_id)
        crowgram_ai.add_event_handler(misc.add_contact)
        crowgram_ai.add_event_handler(misc.delete_contact)
        crowgram_ai.add_event_handler(misc.checking)
        crowgram_ai.add_event_handler(misc.get_restricted_content)
        crowgram_ai.add_event_handler(misc.get_pm_log)
        crowgram_ai.add_event_handler(misc.get_mention_log)
        crowgram_ai.add_event_handler(misc.check_user_history)
        crowgram_ai.add_event_handler(misc.set_helper)
        crowgram_ai.add_event_handler(misc.crowgram_help)
        crowgram_ai.add_event_handler(misc.run_updater)

def run_assistant_handlers():
    with crowgram_assistant as assistant:
        assistant.add_event_handler(music.connect_user)
        assistant.add_event_handler(music.disconnect_user)
        assistant.add_event_handler(music.show_approved_list)
        assistant.add_event_handler(music.play_audio)
        assistant.add_event_handler(music.pause_audio)
        assistant.add_event_handler(music.resume_audio)
        assistant.add_event_handler(music.end_audio)

    crowgram.start()
    crowgram_bot.start()
    crowgram_assistant.start()
    print("Crowgram Started")
    crowgram_image = "https://telegra.ph/file/700b7f318d380cb2d228d.jpg"
    crowgram.send_file(log_group, crowgram_image, caption=f"Your Crowgram has been started successfully.\n\n╭─⊸ Crowgram Version: {utils.crowgram_version}\n├─⊸ Python Version: {python_version()}\n├─⊸ Telethon Version: {version.__version__}\n╰─⊸ PyTgCalls Version: {__version__}\n\nThank You,\nCrowgram")
    try:
        crowgram.run_until_disconnected()
    finally:
        crowgram.disconnect()