import csv

class ContactList:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_contacts(self):
        contacts = []
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
        return contacts
    
    def write_contacts(self, contacts):
        fieldnames = ['First Name', 'Favorite Fruit', 'Favorite Color']
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contacts)
    
    def add_contact(self):
        name = input("Enter First Name: ")
        fruit = input("Enter Favorite Fruit: ")
        color = input("Enter Favorite Color: ")
        new_contact = {'First Name': name, 'Favorite Fruit': fruit, 'Favorite Color': color}
        contacts = self.read_contacts()
        contacts.append(new_contact)
        self.write_contacts(contacts)
        print(f"{name} added to contacts!")

    def list_contacts(self):
        contacts = self.read_contacts()
        if len(contacts) == 0:
            print("You have no contacts.")
        else:
            for contact in contacts:
                print(contact)
    
    def update_contact(self):
        name = input("Enter contact name to update: ")
        contacts = self.read_contacts()
        found = False
        for contact in contacts:
            if contact['First Name'] == name:
                new_name = input("Enter name: ")
                new_fruit = input("Enter Favorite Fruit: ")
                new_color = input("Enter Favorite Color: ")
                contact['First Name'] = new_name
                contact['Favorite Fruit'] = new_fruit
                contact['Favorite Color'] = new_color
                found = True
                break
        if found:
            self.write_contacts(contacts)
            print("Contact updated!")
        else:
            print(f"Contact {name} not found...")

    def delete_contact(self):
        name = input('Enter contact name to delete: ')
        contacts = self.read_contacts()
        found = False
        for contact in contacts:
            if contact['First Name'] == name:
                contacts.remove(contact)
                found = True
                break
        if found:
            self.write_contacts(contacts)
            print(f'{name} deleted from contacts!')
        else:
            print(f'Contact {name} not found...')
    
    def run(self):
        while True:
            print("""\n----- Contact List -----\n
                  1. View Contacts\n
                  2. Add Contact\n
                  3. Update Contact\n
                  4. Delete Contact\n
                  5. Quit\n
                  """)
            choice = input("Enter choice (1-5): ")

            match choice:
                case '1':
                    self.list_contacts()
                case '2':
                    self.add_contact()
                case '3':
                    self.update_contact()
                case '4':
                    self.delete_contact()
                case '5':
                    break
                case _:
                    print('Invalid entry...')

if __name__ == '__main__':
    contact_list = ContactList('contacts.csv')
    contact_list.run()