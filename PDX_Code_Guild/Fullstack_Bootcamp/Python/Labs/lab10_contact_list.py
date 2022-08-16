# ....Lab 10 Version 1 ~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~

import re

# with open('C:/users/johns/desktop/contact_list.csv', 'r') as file:
#     lines = file.read().split('\n')
#     # print(lines)

# contacts = []

# header =  True
# for line in lines:
#     if header:
#         keys = ''.join(line).split(',')
#         header = False
#     else:
#         values = ''.join(line).split(',')
#         contacts.append({keys[i]:values[i] for i in range(len(keys))})


# print(contacts)

# ....Lab 10 Version 2 ~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~

# CRUD REPL

def csv_crud_repl(file_path, mode):
    with open (file_path, mode) as file:
        lines = file.read().split('\n')

    contacts = []
    
# Reads csv and converts to list of dicts.
    header =  True
    for line in lines:
        if header:
            keys = ''.join(line).split(',')
            header = False
        else:
            values = ''.join(line).split(',')
            contacts.append({keys[i]:values[i] for i in range(len(keys))})
    
# Beginning of CRUD REPL, takes user input key to initiate conditional functions (that don't really need to be functions in this format..).
    user_prompt = ''

    while user_prompt != 'x':
        user_prompt = input("""What would you like to do? 
        v = View contact list
        c = Create a new contact
        r = Retrieve a contact
        u = Update a contact
        d = Delete a contact
        s = Save contact list
        x = Exit program
        """)
# Print of current contacts.
        if user_prompt == 'v':
            print(contacts)
            continue
# Creation and addition of new contact.
        elif user_prompt == 'c':
            def create():
                new_values = input('Please state: Name, Favorite Color, Favorite Fruit: ')
                new_values = list(new_values.split(','))
                values.append(new_values)
                contacts.append({keys[i]:new_values[i] for i in range(len(keys))})
                print(contacts)
            create()
            continue
# Retrieval and display of existing contact.
        elif user_prompt == 'r':
            def retrieve():
                contact_name = input('State the name of the contact you want to retrieve: ')
                for contact in contacts:
                    if contact_name == contact['name']:
                        print(contact)
                        return contact        
            retrieve()
            continue
# Update existing contact with new attributes.
        elif user_prompt == 'u':
            def update():
                contact_name = input('State the name of the contact you want to update: ')
                for contact in contacts:
                    if contact_name == contact['name']:
                        print(contact)
                        update = input('Which attribute would you like to update? ')
                        contact[update] = input('Type updated information: ')
                        print(contact)
                        return contact
            update()
            continue
# Deletion of a selected contact from the list.
        elif user_prompt == 'd':
            def delete():
                contact_name = input('State the name of the contact you want to delete: ')
                for contact in contacts:
                    if contact_name == contact['name']:
                        check = input(f'{contact} will be deleted. Are you certain? y/n ')
                        if check == 'y':
                            contacts.remove(contact)
                        elif check == 'n':
                            pass
                        # print(contacts)
                        return(contacts)
            delete()
            continue
                    
# ....Lab 10 Version 3 ~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~

# Ability to save updated csv file at path.
        elif user_prompt == 's' or 'x':
            print('Saving file...')
            lines = [','.join(keys)]
            for contact in contacts:
                new_string = ','.join(contact.values())
                lines.append(new_string)
            contact_list = '\n'.join(lines)
            with open(file_path, 'w') as file:
                file.write(contact_list)


csv_crud_repl('contacts.csv', 'r')






