import csv

from messages_sender.model.Contact import Contact


def read_contacts(file_path: str):
    file = open(file_path)
    csvreader = csv.reader(file)

    next(csvreader)
    contacts = []
    for row in csvreader:
        contact = Contact(id=int(row[0]), name=row[1], cell_phone=row[2], email=row[3])
        contacts.append(contact)
    file.close()

    return contacts
