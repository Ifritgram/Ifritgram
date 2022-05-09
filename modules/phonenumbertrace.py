from telethon import events
from time import sleep
import phonenumbers
from phonenumbers import timezone, geocoder, carrier


@events.register(events.NewMessage(outgoing=True, pattern=r"\.pntrace"))
async def runpntrace(event):
    getphonenumber = event.message.raw_text.split()
    targetphonenumber = getphonenumber[1]
    messagelocation = event.to_id
    await event.edit("Tracing...")
    sleep(2)
    await event.delete()
    try:
        details = phonenumbers.parse(targetphonenumber)
        targettimezone = timezone.time_zones_for_number(details)
        targetcarrier = carrier.name_for_number(details, "en")
        targetregion = geocoder.description_for_number(details, "en")
        await event.client.send_message(
            messagelocation,
            f"Target Phone Number: {targetphonenumber}\nTimezone: {targettimezone}\nCarrier: {targetcarrier}\nRegion: {targetregion}",
        )
    except:
        pass
