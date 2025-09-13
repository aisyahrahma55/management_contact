'Open and Save Document File'

def open_contact(path='contact.txt'):
    with open(path, 'r') as f:
        contact = f.readlines()
    return contact

def save_contact(path='contact.txt', line=[]):
    with open(path, 'w') as f:
        f.writelines(line)