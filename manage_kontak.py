"Management Contact Program"
import contact
def main():
    office_contact = contact.contact()
    family_contact = contact.contact()


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

if __name__ == '__main__':
    main()