import os

import pytest

from messages_sender import message_sender


@pytest.fixture
def sms_sender(mocker):
    return mocker.patch("messages_sender.services.sms_sender.send_message")


def test_send_messages(sms_sender):
    contacts_file_path = os.path.realpath("../resources/contacts.csv")
    message_template_file_path = os.path.realpath("../resources/message-template.txt")
    message_sender.send_messages(contacts_file_path, message_template_file_path, "sms")

    assert sms_sender.called is True
