from telethon import events
from speedtest import Speedtest


@events.register(events.NewMessage(outgoing=True, pattern=r"\.st"))
async def runst(event):
    messagelocation = event.to_id
    await event.edit("Speedtest Of Ridogram Server Has Started...")
    try:
        starttest = Speedtest()
        await event.edit("Loading Servers List...")
        starttest.get_servers()
        await event.edit("Choosing Best Server...")
        bestserver = starttest.get_best_server()
        await event.edit("Calculating Download Speed...")
        downloadspeedtest = starttest.download()
        await event.edit("Calculating Upload Speed...")
        uploadspeedtest = starttest.upload()
        await event.edit("Report Is Being Prepared...")
        downloadreport = f"{downloadspeedtest / 1024 / 1024:.2f}"
        uploadreport = f"{uploadspeedtest / 1024 / 1024:.2f}"
        await event.delete()
        await event.client.send_message(
            messagelocation,
            f"Download Speed: {downloadreport} Mbit/s\nUpload Speed: {uploadreport} Mbit/s\nLatency: {bestserver['latency']} ms\nHost: {bestserver['host']}\nLocation: {bestserver['name']}, {bestserver['country']}",
        )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
