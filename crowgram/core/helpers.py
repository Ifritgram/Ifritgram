from telethon.tl.custom import Button

display_menu = [
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
        Button.inline("Translator", b'translator'),
        Button.inline("Who", b'who'),
        Button.inline("Updater", b'updater')
    ],
    [
        Button.url("Crowgram Chat", url="https://t.me/crowgramchat")
    ]
]

back = [
    [
        Button.inline("Back", b'back')
    ]
]