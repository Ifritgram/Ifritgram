from telethon import events
from os import system, remove


@events.register(events.NewMessage(outgoing=True, pattern=r"\.cpis"))
async def runcpis(event):
    await event.edit("Processing...")
    try:
        ridogramuserdetails = await event.get_sender()
        ridogramuserid = ridogramuserdetails.id
        ridogramusername = ridogramuserdetails.first_name
        event.client.parse_mode = "html"
        userdatafile = "ridogramuserdata.txt"
        sprungefile = "sprungedata.txt"
        fetchcontent = await event.get_reply_message()
        datafile = open(userdatafile, "w")
        datafile.write(f"{fetchcontent.message}")
        datafile.close()
        system(
            f"cat {userdatafile} | curl -F 'sprunge=<-' http://sprunge.us > {sprungefile}"
        )
        sprungedatafile = open(sprungefile, "r")
        readsprungedatafile = sprungedatafile.read()
        sprungedatafile.close()
        await event.edit(
            f"Content Link: {readsprungedatafile}\nUpload By: <a href='tg://user?id={ridogramuserid}'>{ridogramusername}</a>"
        )
        remove(userdatafile)
        remove(sprungefile)
    except:
        await event.edit("Something Went Wrong")
