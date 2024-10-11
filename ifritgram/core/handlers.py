import core.client
from plugins import default, helper, misc

ifritgram = core.client.ifritgram

def run_handlers():
    with ifritgram as ifrit:
        ifrit.add_event_handler(helper.execute_helper)
        ifrit.add_event_handler(helper.query_response)
        ifrit.add_event_handler(default.ping_the_server)
        ifrit.add_event_handler(misc.get_self_destructive_media)

    ifritgram.start()
    print("Ifritgram Started")
    try:
        ifritgram.run_until_disconnected()
    finally:
        ifritgram.disconnect()