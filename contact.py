'Class contact for running management contact project'
import document


class contact:
    def __init__(self):
        self.contact = document.open_contact()

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
        document.save_contact(line=self.contact)
