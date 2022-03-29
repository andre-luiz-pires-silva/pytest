from messages_sender.model import Contact


def send_message(contact: Contact, message: str):
    __fake_send_sms(contact, message)


def __fake_send_sms(contact: Contact, message: str):
    print(f"Send SMS to {contact.cell_phone}: {message}")