from telethon import events
from whois import whois


@events.register(events.NewMessage(outgoing=True, pattern=r"\.whois"))
async def runwhois(event):
    await event.delete()
    messagelocation = event.to_id
    domainname = event.message.raw_text.split()
    try:
        setdomain = domainname[1]
        initialized = whois(setdomain)
        target_customer_name = initialized.name
        target_customer_organization = initialized.org
        target_customer_address = initialized.address
        target_customer_city = initialized.city
        target_customer_state = initialized.state
        target_customer_zipcode = initialized.zipcode
        target_customer_country = initialized.country
        target_customer_emails = initialized.emails
        target_domain_name = initialized.domain_name
        target_domain_registrar_company = initialized.registrar
        target_domain_registrar_server = initialized.whois_server
        target_domain_registration_date = initialized.creation_date
        target_domain_expiration_date = initialized.expiration_date
        target_domain_updated_date = initialized.updated_date
        target_domain_status = initialized.status
        target_domain_name_servers = initialized.name_servers
        await event.client.send_message(
            messagelocation,
            f"Customer Name: {target_customer_name}\nCustomer Organization: {target_customer_organization}\nCustomer Address: {target_customer_address}\nCustomer City: {target_customer_city}\nCustomer State: {target_customer_state}\nCustomer Zipcode: {target_customer_zipcode}\nCustomer Country: {target_customer_country}\nCustomer Emails: {target_customer_emails}\nDomain Name: {target_domain_name}\nRegistrar Company: {target_domain_registrar_company}\nRegistrar Server: {target_domain_registrar_server}\nRegistraion Date: {target_domain_registration_date}\nExpired Date: {target_domain_expiration_date}\nUpdated On: {target_domain_updated_date}\nStatus: {target_domain_status}\nName Servers: {target_domain_name_servers}",
        )
    except:
        pass
