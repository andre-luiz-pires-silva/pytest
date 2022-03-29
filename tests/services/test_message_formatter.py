from messages_sender.model.Contact import Contact
from messages_sender.services import message_formatter


def test_format_message():
    message_template = "template {{name}}"
    contact = Contact(id=0, name="test", cell_phone="", email="")

    formatted_message = message_formatter.format_message(message_template, contact)

    assert formatted_message == f"template {contact.name}"
