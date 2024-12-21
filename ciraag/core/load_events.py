from ciraag.core.client import ciraag
from ciraag.plugins import default
from .handlers_name import default_ciraag_plugins

def ciraag_events():
    with ciraag as ciraag_userbot:
        for handler_name in default_ciraag_plugins:
            plugin = f"{handler_name}"
            ciraag_userbot.add_event_handler(getattr(default, plugin))