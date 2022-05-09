from telethon import events
from time import sleep
from email_validator import validate_email, EmailNotValidError


@events.register(events.NewMessage(outgoing=True, pattern=r"\.ev"))
async def runev(event):
    await event.edit("Checking...")
    sleep(2)
    getemailaddress = await event.get_reply_message()
    try:
        valid = validate_email(getemailaddress.message)
        if valid.email:
            await event.edit(
                f"{getemailaddress.message} Is Valid Email Address"
            )
    except EmailNotValidError as error:
        await event.edit(f"{str(error)}")
    except:
        pass
