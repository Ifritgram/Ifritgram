import core.client
import os
import plugins
from telethon import sync
from telethon import version
from platform import python_version

crowgram = core.client.crowgram
crowgram_bot = core.client.crowgram_bot
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
        crowgram_ai.add_event_handler(plugins.run_translator)
        crowgram_ai.add_event_handler(plugins.check_user_history)
        crowgram_ai.add_event_handler(plugins.crowgram_help)
        crowgram_ai.add_event_handler(plugins.run_updater)

    crowgram.start()
    crowgram_bot.start()
    print("Crowgram Started")
    crowgram_image = "https://telegra.ph/file/700b7f318d380cb2d228d.jpg"
    crowgram.send_file(log_group, crowgram_image, caption=f"Your Crowgram has been started successfully.\n\n╭─⊸ Crowgram Version: 1.23.6\n├─⊸ Python Version: {python_version()}\n╰─⊸ Telethon Version: {version.__version__}\n\nThank You,\nCrowgram")
    crowgram.run_until_disconnected()