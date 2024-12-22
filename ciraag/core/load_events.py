from ciraag.core.client import ciraag
from ciraag.plugins import default, misc, helper
from .handlers_name import default_ciraag_plugins, misc_ciraag_plugins, help_ciraag_plugins

def ciraag_events():
    with ciraag as ciraag_userbot:
        for handler_name in default_ciraag_plugins:
            plugin = f"{handler_name}"
            ciraag_userbot.add_event_handler(getattr(default, plugin))
            
        for handler_name in misc_ciraag_plugins:
            plugin = f"{handler_name}"
            ciraag_userbot.add_event_handler(getattr(misc, plugin))
        
        for handler_name in help_ciraag_plugins:
            plugin = f"{handler_name}"
            ciraag_userbot.add_event_handler(getattr(helper, plugin))