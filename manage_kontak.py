"Management Contact Program"

contact1 = {'name': "Jorge", 'phone': '680000000', 'email': 'Joe@python.com'}
contact2 = {'name': "George", 'phone': '68000001','email': 'George@python.com'}
contact = [contact1, contact2]

while True:
    print('\nMENU KONTAK')
    print('1 - List all users')
    print('2 - Add new user and Edit user')
    print('3 - Delete user')
    print('4 - Exit')

    choice = input('\nEnter your choice: ')

    if choice == '1':
        #List new user
        if contact:
            for num, item in enumerate(contact, start=1):
                print(f'\n{num}. {item["name"]} : {item["phone"]} : {item["email"]}')
        else:
            print('\nNo user added')
            continue
    elif choice == '2':
        #Add new user and edit user
        name = input('\nEnter your name: ')
        phone = input('\nEnter your phone: ')
        email = input('\nEnter your email: ')
        new_contact = {'name': name, 'phone': phone, 'email': email}
        contact.append(new_contact)
        print('\nUser added successfully!')
    elif choice == '3':
        #Delete user
        for num, item in enumerate(contact, start=1):
            print(f'\n{num}. {item["name"]} : {item["email"]}')

        delete_contact = int(input('\nEnter your choice: '))
        del contact[delete_contact-1]
        print('\nUser deleted successfully!')
    elif choice == '4':
        break
    else:
        print('Invalid choice')
