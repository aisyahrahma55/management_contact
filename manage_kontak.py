"Management Contact Program"

def open_contact(path='contact.txt'):
    with open(path, 'r') as f:
        contact = f.readlines()
    return contact

def save_contact(path='contact.txt', line=[]):
    with open(path, 'w') as f:
        f.writelines(line)

class contact:
    def __init__(self):
        self.contact = open_contact()

    def main(self):
        if self.contact:
            for num, item in enumerate(self.contact, start=1):
                print(f'{num}.'+item)
        else:
            print('\nNo user added')
            return 1

    def add_contact(self):
        name = input('\nEnter your name: ')
        phone = input('\nEnter your phone: ')
        email = input('\nEnter your email: ')
        new_contact = f'{name} {phone} {email}'+'\n'
        self.contact.append(new_contact)
        print('\nUser added successfully!')

    def delete(self):
        if self.main() == 1:
            return
        else:
            try:
                delete_contact = int(input('\nEnter your choice: '))
                del self.contact[delete_contact - 1]
                print('\nUser deleted successfully!')
            except:
                print('\nNo user added')

    def exit(self):
        save_contact(line=self.contact)

office_contact = contact()
family_contact = contact()

while True:
    print('\nMENU KONTAK')
    print('1 - List all users')
    print('2 - Add new user')
    print('3 - Delete user')
    print('4 - Exit')

    choice = input('\nEnter your choice: ')

    if choice == '1':
        #List new user
        office_contact.main()
    elif choice == '2':
        #Add new user
        office_contact.add_contact()
    elif choice == '3':
        #Delete user
        office_contact.delete()
    elif choice == '4':
        #Exit contact
        office_contact.exit()
        break
    else:
        print('Invalid choice')