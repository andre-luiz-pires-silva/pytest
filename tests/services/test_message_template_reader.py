import os
from messages_sender.services import message_template_reader


def test_read_message_template():
    file_path = os.path.realpath("resources/message-template.txt")
    message_template = message_template_reader.read_message_template(file_path)

    assert message_template == "Test {{name}}."
