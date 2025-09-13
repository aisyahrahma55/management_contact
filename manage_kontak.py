"Management Contact Program"

class contact:
    def __init__(self):
        self.contact = []

    def main(self):
        if self.contact:
            for num, item in enumerate(self.contact, start=1):
                print(f'\n{num}. {item["name"]} : {item["phone"]} : {item["email"]}')
        else:
            print('\nNo user added')
            return 1

    def add_contact(self):
        name = input('\nEnter your name: ')
        phone = input('\nEnter your phone: ')
        email = input('\nEnter your email: ')
        new_contact = {'name': name, 'phone': phone, 'email': email}
        self.contact.append(new_contact)
        print('\nUser added successfully!')

    def delete(self):
        if self.main() == 1:
            return
        else:
            delete_contact = int(input('\nEnter your choice: '))
            del contact[delete_contact - 1]
            print('\nUser deleted successfully!')

office_contact = contact()
family_contact = contact()

while True:
    print('\nMENU KONTAK')
    print('1 - List all users')
    print('2 - Add new user and Edit user')
    print('3 - Delete user')
    print('4 - Exit')

    choice = input('\nEnter your choice: ')

    if choice == '1':
        #List new user
        office_contact.main()

    elif choice == '2':
        #Add new user and edit user
        office_contact.add_contact()

    elif choice == '3':
        #Delete user
        office_contact.delete()
    elif choice == '4':
        break
    else:
        print('Invalid choice')