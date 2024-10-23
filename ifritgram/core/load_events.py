import core.client
from plugins import default, helper, misc, fighter
from .handlers_name import default_plugins, helper_plugins, misc_plugins, fighter_plugins

ifritgram = core.client.ifritgram

def ifritgram_events():
    with ifritgram as ifrit:
        for handler_name in default_plugins:
            plugin = f"{handler_name}"
            ifrit.add_event_handler(getattr(default, plugin))
        
        for handler_name in helper_plugins:
            plugin = f"{handler_name}"
            ifrit.add_event_handler(getattr(helper, plugin))
        
        for handler_name in misc_plugins:
            plugin = f"{handler_name}"
            ifrit.add_event_handler(getattr(misc, plugin))
        
        for handler_name in fighter_plugins:
            plugin = f"{handler_name}"
            ifrit.add_event_handler(getattr(fighter, plugin))