from telethon import events
import requests
import base64


@events.register(events.NewMessage(outgoing=True, pattern=r"\.wu"))
async def runwu(event):
    await event.edit("Checking...")
    messagelocation = event.to_id
    getlocation = event.message.raw_text.splitlines()
    replacedata = getlocation[0].replace(".wu ", "")
    userlocation = replacedata.splitlines()
    try:

        class keyinformation:
            weatherkey = ""

            def __init__(self, weatherkey):
                self.weatherkey = weatherkey

        mainkey = keyinformation(
            "NmE5OTlhNTE2NWFmNzQ2NzAxMzg1YjdlMTRkOTc5YTg="
        )

        class getweatherinformation:
            secretkey = mainkey.weatherkey
            weatherkeybytes = secretkey.encode("ascii")
            revealkey = base64.b64decode(weatherkeybytes)
            decoderevealkeybytes = revealkey.decode("ascii")
            weatherupdate = f"https://api.openweathermap.org/data/2.5/weather?q={userlocation[0]}&appid={decoderevealkeybytes}"
            getdata = requests.get(weatherupdate)
            maindata = getdata.json()

        weatherdata = getweatherinformation()
        if weatherdata.maindata["cod"] == "404":
            await event.delete()
            await event.client.send_message(
                messagelocation, "Location Not Found"
            )
        else:
            temp_city = (weatherdata.maindata["main"]["temp"]) - 273.15
            weatherdescription = weatherdata.maindata["weather"][0][
                "description"
            ]
            currenthumidity = weatherdata.maindata["main"]["humidity"]
            currentwind = weatherdata.maindata["wind"]["speed"]
            weathercity = weatherdata.maindata["name"]
            weathercountry = weatherdata.maindata["sys"]["country"]
            await event.delete()
            await event.client.send_message(
                messagelocation,
                f"Weather Location: {weathercity}, {weathercountry}\nTemperature: {temp_city:.2f} °C\nWeather Description: {weatherdescription.title()}\nHumidity: {currenthumidity}%\nWind: {currentwind} km/h",
            )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
