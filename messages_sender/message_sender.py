from messages_sender.services import contacts_reader
from messages_sender.services import message_template_reader
from messages_sender.services import message_formatter
from messages_sender.services import sender_resolver


def send_messages(contact_file_path, message_template_path, message_type):
    sender = sender_resolver.get_sender_by_message_type(message_type)
    contacts = contacts_reader.read_contacts(contact_file_path)
    message_template = message_template_reader.read_message_template(message_template_path)
    for contact in contacts:
        formatted_message = message_formatter.format_message(message_template, contact)
        sender.send_message(contact, formatted_message)
