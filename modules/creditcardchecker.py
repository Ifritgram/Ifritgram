from telethon import events
from credit_card_checker import CreditCardChecker
from time import sleep


@events.register(events.NewMessage(outgoing=True, pattern=r"\.n"))
async def runn(event):
    await event.edit("Checking...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    getcreditcardnumber = event.message.raw_text.splitlines()
    replacedata = getcreditcardnumber[0].replace(".n ", "")
    creditcardnumberis = replacedata.splitlines()
    try:
        if CreditCardChecker(f"{creditcardnumberis[0]}").valid():
            await event.client.send_message(
                messagelocation,
                f"Congratulations, {creditcardnumberis[0]} Is Valid.",
            )
        else:
            await event.client.send_message(
                messagelocation, f"Sorry, {creditcardnumberis[0]} Is Invalid."
            )
    except:
        pass
