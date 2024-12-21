from ciraag.core.client import ciraag
from ciraag.core.load_events import ciraag_events

class StartCiraag:
    def __init__(self):
        ciraag_events()
        ciraag.start()
        print("Ciraag Started")
        try:
            ciraag.run_until_disconnected()
        finally:
            ciraag.disconnect()

start_ciraag = StartCiraag()