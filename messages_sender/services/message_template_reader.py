def read_message_template(file_path: str):
    file = open(file_path)
    message_template = file.read()
    file.close()
    return message_template
