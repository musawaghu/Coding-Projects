import pickle
from Contact import *

phone_numbers = []


# return the unpickled dictionary if it exists in the file 'mydata.dat',
# or return an empty dictionary if the file doesn't exist
def load_contacts():
    try:
        with open('mydata.dat', 'rb') as file:
            contact_dictionary = pickle.load(file)
    except FileNotFoundError:
        # If file doesn't exist, create and return an empty dictionary
        contact_dictionary = {}

    return contact_dictionary


def save_contacts(contacts):
    with open('mydata.dat', 'wb') as file:
        pickle.dump(contacts, file)


"""
The add function asks the user to create one Contact object to place in the dictionary of Contacts.  
They should be asked for a name, a list of phone numbers, and an email address.
If a Contact with the given name does not exist in contacts, add it. 
Otherwise, we’ll inform the user that a Contact with that name already exists.
"""


def add(contacts):
    name = input("Name: ")
    if name in contacts:
        print("That name already exists!")
        return

    while True:
        next_num = input("Enter a phone number or -1 to stop: ")
        if next_num == '-1':
            break
        phone_numbers.append(next_num)

    email = input("Email: ")

    entry = Contact(name, phone_numbers, email)
    contacts[name] = entry


def look_up(contacts):
    name = input("Enter a name: ")
    if name in contacts:
        print(contacts[name])
    else:
        print("That name is not found")


def delete(contacts):
    name = input("Enter a contact to delete: ")
    if name in contacts:
        contacts.pop(name)
    else:
        print("That name is not found")


def change(contacts):
    name = input("Enter a contact to change: ")
    if name in contacts:
        while True:
            choice = input(
                "Enter a choice (1 to remove a phone number, 2 to add a phone number, 3 to change the email address, 4 to change the name, 5 to quit: ")
            if choice == '1':
                remove_pn = input("Enter the phone number you want to remove: ")
                if remove_pn in phone_numbers:
                    phone_numbers.remove(remove_pn)
            elif choice == '2':
                add_pn = input("Enter the phone number you want to add: ")
                phone_numbers.append(add_pn)
            elif choice == '3':
                email_change = input("Enter the email address you want to change to: ")
                entry = Contact(name, phone_numbers, email_change)
                contacts[name] = entry
            elif choice == '4':
                name_change = input("Enter the name you want to change to: ")
                del contacts[name]
                while True:
                    next_num = input("Enter a phone number or -1 to stop: ")
                    if next_num == '-1':
                        break
                    phone_numbers.append(next_num)

                email = input("Email: ")

                entry = Contact(name, phone_numbers, email)
                contacts[name] = entry
            elif choice == '5':
                break
            else:
                print("Invalid choice!")
    else:
        print("The name you want to change is not saved in contacts")


def main():
    contacts = load_contacts()

    # Allow the user to interact with the dictionary of contacts

    while True:
        choice = input("Enter a choice (1 to add a contact, 2 to look up a contact, 3 to delete a contact, 5 to quit: ")
        if choice == '1':
            add(contacts)
        elif choice == '2':
            look_up(contacts)
        elif choice == '3':
            delete(contacts)
        elif choice == '4':
            change(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

    save_contacts(contacts)


main()
