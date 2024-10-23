import core.client
from .load_events import ifritgram_events

ifritgram = core.client.ifritgram

def run_handlers():
    ifritgram_events()
    ifritgram.start()
    print("Ifritgram Started")
    try:
        ifritgram.run_until_disconnected()
    finally:
        ifritgram.disconnect()