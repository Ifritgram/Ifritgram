import core.client
import os
import plugins
import player
import utils
from telethon import sync
from telethon import version
from platform import python_version

crowgram = core.client.crowgram
crowgram_bot = core.client.crowgram_bot
crowgram_assistant = core.client.crowgram_assistant
log_group = int(os.environ["log_group"])

def run_handlers():
    with crowgram as crowgram_ai:
        crowgram_ai.add_event_handler(plugins.check_alive)
        crowgram_ai.add_event_handler(plugins.pinged)
        crowgram_ai.add_event_handler(plugins.get_id)
        crowgram_ai.add_event_handler(plugins.add_contact)
        crowgram_ai.add_event_handler(plugins.delete_contact)
        crowgram_ai.add_event_handler(plugins.checking)
        crowgram_ai.add_event_handler(plugins.get_restricted_content)
        crowgram_ai.add_event_handler(plugins.get_pm_log)
        crowgram_ai.add_event_handler(plugins.get_mention_log)
        crowgram_ai.add_event_handler(plugins.check_user_history)
        crowgram_ai.add_event_handler(plugins.crowgram_help)
        crowgram_ai.add_event_handler(plugins.run_updater)

def run_assistant_handlers():
    with crowgram_assistant as assistant:
        assistant.add_event_handler(player.play_audio)
        assistant.add_event_handler(player.pause_audio)
        assistant.add_event_handler(player.resume_audio)
        assistant.add_event_handler(player.end_audio)

    crowgram.start()
    crowgram_bot.start()
    crowgram_assistant.start()
    print("Crowgram Started")
    crowgram_image = "https://telegra.ph/file/700b7f318d380cb2d228d.jpg"
    crowgram.send_file(log_group, crowgram_image, caption=f"Your Crowgram has been started successfully.\n\n╭─⊸ Crowgram Version: {utils.crowgram_version}\n├─⊸ Python Version: {python_version()}\n╰─⊸ Telethon Version: {version.__version__}\n\nThank You,\nCrowgram")
    try:
        crowgram.run_until_disconnected()
    finally:
        crowgram.disconnect()