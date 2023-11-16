#! python3
# a contact book
import pprint, contact

def main():
    global contacts

    contacts = contact.contact
    if contacts == {}:
        print('''You do not have any contacts yet.
    Do you want to add some?
            y = yes, n = no''')
        ans = input().lower()
        if ans in ['yes', 'y']:
            addContacts()
        elif ans in ['no', 'n']:
            exit()
        else:
            print('That is not an option')
            main()
    else:
        for a, b in contacts.items():
            print(a,':',b)
        print('''Do you want to edit or delete a contact?
            e = Edit, d = delete, n = no''')
        ans2 = input().lower()
        if ans2 in ['e', 'edit']:
            editContacts()
        elif ans2 in ['d', 'delete']:
            deleteContacts()
        elif ans2 in ['no', 'n']:
            exit()
        else:
            print('That is not an option')
            exit()

def addContacts():
    global contacts

    name = input('Name: ')
    number = input('Number: ')
    contacts.setdefault(name, number)
    for a, b in contacts.items():
        print(a,':',b)
    save()

def editContacts():
    global contacts

    contactName = input('Enter the name of the contact: ').lower()
    if contactName not in contacts.keys():
        print('''You do not have this contact.
Do you want to add this contact?
        y = yes, n = no, x to exit''')
        ans3 = input().lower()
        if ans3 in ['yes', 'y']:
            addContacts()
        elif ans3 in ['no', 'n']:
            editContacts()
        elif ans3 == 'x':
            exit()
        else:
            print('That is not an option')
            editContacts()
    else:
        print(contactName)
        print(contacts[contactName] + '\n')
        print('''type 'n' to edit the name,
'p' to edit the number,
'np' to edit both.''')
        ans4 = input().lower()
        if ans4 in ['n', 'name']:
            print(contactName)
            newName = input('Enter the new name of the contact: ')
            contactName = newName
        elif ans4 in ['p', 'phone', 'phonenumber', 'phone number']:
            print(contacts[contactName])
            newNumber = input('Enter the new number of the contact: ')
            contacts[contactName] = newNumber
        elif ans4 == 'np':
            print(contactName, ':', contacts[contactName])
            newName = input('Enter the new name of the contact: ')
            newNumber = input('Enter the new number of the contact: ')
            contactName = newName
            contacts[contactName] = newNumber
        else:
            print('That is not an option.')
            editContacts()
    save()

def deleteContacts():
    global contacts

    print('''c = 'delete a particular contact'
a = delete all contacts.
x = exit''')
    ans5 = input().lower
    if ans5 == 'c':
        contactName = input('Enter the name of the contact: ').lower()
        if contactName not in contacts.keys():
            print('''You do not have this contact.
    Do you want to add this contact?
            y = yes, n = no, x to exit''')
            ans6 = input().lower()
            if ans6 in ['yes', 'y']:
                addContacts()
            elif ans6 in ['no', 'n']:
                deleteContacts()
            elif ans6 == 'x':
                exit()
            else:
                print('That is not an option')
                deleteContacts()
        else:
            contacts.pop(contactName)
            print('deleted')
    elif ans5 == 'a':
        print('You will be deleting all your contacts! type a to exit(), b to delete all contacts')
        ans7 = input().lower()
        if ans7 == 'a':
            exit()
        elif ans7 == 'b':
            contacts.clear()
        else:
            print('That is not an option')
            deleteContacts()
    elif ans5 in ['x', 'exit']:
        exit()
    else:
        print('That is not an option')
        deleteContacts()
    save()

def save():
    global contacts

    pprint.pformat(contacts)
    fileobj = open('contact.py', 'w')
    fileobj.write('contact = ' + pprint.pformat(contacts) + '\n')
    fileobj.close()

main()
