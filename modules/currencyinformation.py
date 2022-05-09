from telethon import events
from time import sleep
from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter


@events.register(events.NewMessage(outgoing=True, pattern=r"\.ci"))
async def runci(event):
    await event.edit("Checking...")
    sleep(2)
    await event.delete()
    selectoption = event.message.raw_text.split()
    messagelocation = event.to_id
    try:
        if selectoption[1] == "s":
            getinformationaboutcurrency = CurrencyCodes()
            getcurrencyname = selectoption[2]
            currencyname = getinformationaboutcurrency.get_currency_name(
                f"{getcurrencyname}"
            )
            currencysymbol = getinformationaboutcurrency.get_symbol(
                f"{getcurrencyname}"
            )
            await event.client.send_message(
                messagelocation,
                f"Currency Name: {currencyname}\nCurrency Symbol: {currencysymbol}",
            )
        elif selectoption[1] == "cr":
            getcurrencyrates = CurrencyRates()
            rates = getcurrencyrates.get_rate(
                f"{selectoption[2]}", f"{selectoption[3]}"
            )
            await event.client.send_message(messagelocation, f"Rates: {rates}")
        elif selectoption[1] == "btcc":
            getbtcinformation = BtcConverter()
            price = getbtcinformation.get_latest_price(f"{selectoption[2]}")
            await event.client.send_message(
                messagelocation, f"{price} {selectoption[2]}"
            )
        else:
            await event.client.send_message(messagelocation, "Wrong Option")
    except IndexError:
        await event.client.send_message(messagelocation, "Select An Option")
    except:
        pass
