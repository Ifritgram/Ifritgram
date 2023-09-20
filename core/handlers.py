import core.client
import os
from telethon import sync
from telethon import version
from platform import python_version
import plugins.alive, plugins.ping, plugins.id, plugins.protection, plugins.restricted, plugins.logger, plugins.translator, plugins.who, plugins.help, plugins.updater

crowgram = core.client.crowgram
crowgram_bot = core.client.crowgram_bot
log_group = int(os.environ["log_group"])

def run_handlers():
    with crowgram as crowgram_ai:
        crowgram_ai.add_event_handler(plugins.alive.check_alive)
        crowgram_ai.add_event_handler(plugins.ping.pinged)
        crowgram_ai.add_event_handler(plugins.id.get_id)
        crowgram_ai.add_event_handler(plugins.protection.add_contact)
        crowgram_ai.add_event_handler(plugins.protection.delete_contact)
        crowgram_ai.add_event_handler(plugins.protection.checking)
        crowgram_ai.add_event_handler(plugins.restricted.get_restricted_content)
        crowgram_ai.add_event_handler(plugins.logger.get_pm_log)
        crowgram_ai.add_event_handler(plugins.logger.get_mention_log)
        crowgram_ai.add_event_handler(plugins.translator.run_translator)
        crowgram_ai.add_event_handler(plugins.who.check_user_history)
        crowgram_ai.add_event_handler(plugins.help.crowgram_help)
        crowgram_ai.add_event_handler(plugins.updater.run_updater)

    crowgram.start()
    crowgram_bot.start()
    print("Crowgram Started")
    crowgram_image = "https://telegra.ph/file/700b7f318d380cb2d228d.jpg"
    crowgram.send_file(log_group, crowgram_image, caption=f"Your Crowgram has been started successfully.\n\n╭─⊸ Crowgram Version: 1.23.5\n├─⊸ Python Version: {python_version()}\n╰─⊸ Telethon Version: {version.__version__}\n\nThank You,\nCrowgram")
    crowgram.run_until_disconnected()