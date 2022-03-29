from messages_sender.model.Contact import Contact


def format_message(message_template: str, contact: Contact):
    formatted_message = message_template.replace("{{name}}", contact.name)
    return formatted_message
