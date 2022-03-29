from messages_sender.services import sms_sender
from messages_sender.services import email_sender


def get_sender_by_message_type(message_type):
    if message_type == "sms":
        return sms_sender
    elif message_type == "email":
        return email_sender
    raise Exception(f"Message type {message_type} not supported.")
