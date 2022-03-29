import os

from messages_sender.model.Contact import Contact
from messages_sender.services import contacts_reader


def test_read_contacts():
    file_path = os.path.realpath("resources/contacts.csv")
    contacts = contacts_reader.read_contacts(file_path)

    assert contacts == [
        Contact(id=1, name="name-test-1", cell_phone="11111-1111", email="one@daitan.com"),
        Contact(id=2, name="name-test-2", cell_phone="22222-2222", email="two@daitan.com")
    ]
