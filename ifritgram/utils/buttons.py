from telethon.tl.custom import Button

categories_menu = [
    [
        Button.inline("🧩 Misc", b'misc')
    ],
    [
        Button.url("💬 Ifritgram Chat", url="https://t.me/ifritgram_chat")
    ]
]

misc_menu = [
    [
        Button.inline("Ping", b'ping'),
        Button.inline("Timer", b'timer')
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