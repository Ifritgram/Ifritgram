from telethon import events
from time import sleep
import requests
import base64


@events.register(events.NewMessage(outgoing=True, pattern=r"\.mvi"))
async def runmvi(event):
    await event.edit("Tracing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    getmacbyuser = event.message.raw_text.splitlines()
    replacedata = getmacbyuser[0].replace(".mvi ", "")
    victimmac = replacedata.splitlines()
    try:

        class keyinformation:
            mackey = ""

            def __init__(self, mackey):
                self.mackey = mackey

        mainkey = keyinformation(
            "YXRfbEwxNmJyREpCUDhaZGFDNVFzWXVxRE5GWG85MVI="
        )

        class getmacvendorinformation:
            secretkey = mainkey.mackey
            mackeybytes = secretkey.encode("ascii")
            revealkey = base64.b64decode(mackeybytes)
            decoderevealkeybytes = revealkey.decode("ascii")
            macvendordetails = f"https://api.macaddress.io/v1?apiKey={decoderevealkeybytes}&output=json&search={victimmac[0]}"
            getdata = requests.get(macvendordetails)
            maindata = getdata.json()

        macvendordata = getmacvendorinformation()
        targetmacaddress = victimmac[0]
        targetisvalid = macvendordata.maindata["macAddressDetails"]["isValid"]
        targetvirtualmachine = macvendordata.maindata["macAddressDetails"][
            "virtualMachine"
        ]
        targettransmissiontype = macvendordata.maindata["macAddressDetails"][
            "transmissionType"
        ]
        targetadministrationtype = macvendordata.maindata["macAddressDetails"][
            "administrationType"
        ]
        targetwiresharknotes = macvendordata.maindata["macAddressDetails"][
            "wiresharkNotes"
        ]
        victimoui = macvendordata.maindata["vendorDetails"]["oui"]
        victimisprivate = macvendordata.maindata["vendorDetails"]["isPrivate"]
        targetcompanyname = macvendordata.maindata["vendorDetails"][
            "companyName"
        ]
        targetcompanyaddress = macvendordata.maindata["vendorDetails"][
            "companyAddress"
        ]
        targetcompanycountrycode = macvendordata.maindata["vendorDetails"][
            "countryCode"
        ]
        targetblockfound = macvendordata.maindata["blockDetails"]["blockFound"]
        targetborderleft = macvendordata.maindata["blockDetails"]["borderLeft"]
        targetborderright = macvendordata.maindata["blockDetails"][
            "borderRight"
        ]
        targetblocksize = macvendordata.maindata["blockDetails"]["blockSize"]
        targetassignmentblocksize = macvendordata.maindata["blockDetails"][
            "assignmentBlockSize"
        ]
        targetdatecreated = macvendordata.maindata["blockDetails"][
            "dateCreated"
        ]
        targetupdated = macvendordata.maindata["blockDetails"]["dateUpdated"]
        await event.client.send_message(
            messagelocation,
            f"Target MAC Address: {targetmacaddress}\nValid: {targetisvalid}\nVirtual Machine: {targetvirtualmachine}\nTransmission Type: {targettransmissiontype}\nAdministration Type: {targetadministrationtype}\nWireshark Notes: {targetwiresharknotes}\nOUI: {victimoui}\nPrivate: {victimisprivate}\nCompany Name: {targetcompanyname}\nCompany Address: {targetcompanyaddress}\nCountry Code: {targetcompanycountrycode}\nBlock Found: {targetblockfound}\nBorder Left: {targetborderleft}\nBorder Right: {targetborderright}\nBlock Size: {targetblocksize}\nAssignment Block Size: {targetassignmentblocksize}\nCreated: {targetdatecreated}\nUpdated: {targetupdated}",
        )
    except KeyError:
        await event.client.send_message(
            messagelocation, "Invalid MAC Or OUI Address Was Received"
        )
    except:
        await event.client.send_message(
            messagelocation, "Something Went Wrong"
        )
