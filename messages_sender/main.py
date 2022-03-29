import os
import message_sender


if __name__ == '__main__':
    contacts_file_path = os.path.realpath("../resources/contacts.csv")
    message_template_file_path = os.path.realpath("../resources/message-template.txt")
    message_sender.send_messages(contacts_file_path, message_template_file_path, "sms")
