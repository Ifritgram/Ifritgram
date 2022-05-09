from telethon import events
from time import sleep
from selenium import webdriver
from os import remove


@events.register(events.NewMessage(outgoing=True, pattern=r"\.wps"))
async def runwps(event):
    await event.edit("Taking Screenshot...")
    sleep(2)
    await event.delete()
    webpage = event.message.raw_text.split()
    messagelocation = event.to_id
    screenshotfilename = "screenshotbyridogram.png"
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/app/.apt/usr/bin/google-chrome"
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(
            executable_path="/app/.chromedriver/bin/chromedriver",
            chrome_options=chrome_options,
        )
        driver.get(f"{webpage[1]}")
        height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
            "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
            "document.documentElement.offsetHeight);"
        )
        width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
            "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
            "document.documentElement.offsetWidth);"
        )
        driver.set_window_size(width + 125, height + 125)
        driver.save_screenshot(screenshotfilename)
        driver.close()
        await event.client.send_file(messagelocation, screenshotfilename)
        remove(screenshotfilename)
    except:
        pass
