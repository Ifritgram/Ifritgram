from telethon.tl.custom import Button

categories_menu = [
    [
        Button.inline("🧩 Misc", b'misc'),
        Button.inline("🎧 Music", b'music')
    ],
    [
        Button.url("💬 Crowgram Chat", url="https://t.me/crowgramchat")
    ]
]

misc_menu = [
    [
        Button.inline("Alive", b'alive'),
        Button.inline("Ping", b'ping'),
        Button.inline("ID", b'id')
    ],
    [
        Button.inline("Protection", b'protection'),
        Button.inline("Restricted", b'restricted'),
        Button.inline("Logger", b'logger')
    ],
    [
        Button.inline("Who", b'who'),
        Button.inline("Updater", b'updater')
    ],
    [
        Button.inline("Main Menu", b'main_menu')
    ]
]

music_menu = [
    [
        Button.inline("Connect", b'connect'),
        Button.inline("Disconnect", b'disconnect'),
        Button.inline("Authorized", b'authorized')
    ],
    [
        Button.inline("Play", b'play'),
        Button.inline("vPlay", b'vplay'),
        Button.inline("Pause", b'pause')
    ],
    [
        Button.inline("Resume", b'resume'),
        Button.inline("End", b'end')
    ],
    [
        Button.inline("Main Menu", b'main_menu')
    ]
]

back_misc = [
    [
        Button.inline("Back", b'back_misc')
    ]
]

back_music = [
    [
        Button.inline("Back", b'back_music')
    ]
]