import pytest

from messages_sender.services import sms_sender
from messages_sender.services import email_sender
from messages_sender.services import sender_resolver


def test_get_sender_by_message_type_sms():
    sender = sender_resolver.get_sender_by_message_type("sms")

    assert sender == sms_sender


def test_get_sender_by_message_type_email():
    sender = sender_resolver.get_sender_by_message_type("email")

    assert sender == email_sender


def test_get_sender_by_message_type_invalid_type():
    message_type = "invalid"
    with pytest.raises(Exception) as exception:
        sender_resolver.get_sender_by_message_type(message_type)

    assert exception.value.args[0] == f"Message type {message_type} not supported."
