from messages_sender.model import Contact


def send_message(contact: Contact, message: str):
    __fake_send_email(contact, message)


def __fake_send_email(contact: Contact, message: str):
    print(f"Send e-mail to {contact.email}: {message}")
