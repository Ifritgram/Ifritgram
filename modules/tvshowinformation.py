from telethon import events
from time import sleep
import requests


@events.register(events.NewMessage(outgoing=True, pattern=r"\.tvsi"))
async def runtvsi(event):
    await event.edit("Searching...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    getquery = event.message.raw_text.splitlines()
    replacedata = getquery[0].replace(".tvsi ", "")
    tvshowname = replacedata.splitlines()
    try:
        datainformation = (
            f"https://api.tvmaze.com/search/shows?q={tvshowname[0]}"
        )
        getdata = requests.get(datainformation)
        maindata = getdata.json()
        showimage = maindata[0]["show"]["image"]["original"]
        showsummary = maindata[0]["show"]["summary"]
        datavalidationone = showsummary.replace("<p><b>", "")
        datavalidationtwo = datavalidationone.replace("</b>", "")
        datavalidationthree = datavalidationtwo.replace("<p>", "")
        datavalidationfour = datavalidationthree.replace("</p>", "")
        datavalidationfive = datavalidationfour.replace("<b>", "")
        datavalidationsix = datavalidationfive.replace("</p></b>", "")
        showscore = maindata[0]["score"]
        showname = maindata[0]["show"]["name"]
        showtype = maindata[0]["show"]["type"]
        showlanguage = maindata[0]["show"]["language"]
        showgenreszero = maindata[0]["show"]["genres"][0]
        showgenresone = maindata[0]["show"]["genres"][1]
        showgenrestwo = maindata[0]["show"]["genres"][2]
        showstatus = maindata[0]["show"]["status"]
        showruntime = maindata[0]["show"]["runtime"]
        showaverageruntime = maindata[0]["show"]["averageRuntime"]
        showpremiered = maindata[0]["show"]["premiered"]
        showended = maindata[0]["show"]["ended"]
        showofficialsite = maindata[0]["show"]["officialSite"]
        showrating = maindata[0]["show"]["rating"]["average"]
        shownetwork = maindata[0]["show"]["network"]["name"]
        showcountryname = maindata[0]["show"]["network"]["country"]["name"]
        showcountrycodename = maindata[0]["show"]["network"]["country"]["code"]
        showcountrytimezone = maindata[0]["show"]["network"]["country"][
            "timezone"
        ]
        await event.client.send_file(
            messagelocation,
            showimage,
            caption=f"Show Name: {showname}\nShow Summary: {datavalidationsix}\nShow Score: {showscore}\nShow Type: {showtype}\nShow Language: {showlanguage}\nGenres: {showgenreszero} | {showgenresone} | {showgenrestwo}\nShow Status: {showstatus}\nShow Runtime: {showruntime}\nShow Average Runtime: {showaverageruntime}\nShow Premiered: {showpremiered}\nShow Ended: {showended}\nShow Rating: {showrating}\nShow Network: {shownetwork}\nShow Country Name: {showcountryname}\nShow Country Codename: {showcountrycodename}\nShow Country Timezone: {showcountrytimezone}\nShow Official Website: {showofficialsite}",
        )
    except:
        pass
