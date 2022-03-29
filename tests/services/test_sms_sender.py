import pytest
from messages_sender.model.Contact import Contact
from messages_sender.services import sms_sender


@pytest.fixture
def fake_send_email(mocker):
    return mocker.patch("messages_sender.services.sms_sender.__fake_send_sms")


def test_read_contacts(fake_send_email):
    contact = Contact(id=1, name="name-test-1", cell_phone="11111-1111", email="one@daitan.com")
    message = "message"

    sms_sender.send_message(contact, message)

    assert fake_send_email.called is True
    assert fake_send_email.call_args[0][0] == contact
    assert fake_send_email.call_args[0][1] == message




