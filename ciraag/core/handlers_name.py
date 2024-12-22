class CiraagPlugins:
    def __init__(self):
        self.default_plugins = [
            "ping_the_server"
        ]
        self.misc_plugins = [
            "get_self_destructive_media"
        ]
        self.helper_plugins = [
            "execute_helper",
            "set_helper"
        ]

default_ciraag_plugins = CiraagPlugins().default_plugins
misc_ciraag_plugins = CiraagPlugins().misc_plugins
help_ciraag_plugins = CiraagPlugins().helper_plugins