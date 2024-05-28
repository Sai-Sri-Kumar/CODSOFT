from prettytable import PrettyTable
def loadContacts():
    mycontacts = []
    try:
        with open("mycontacts.txt", "r") as file:
            for line in file.readlines():
                my_name, my_number, my_email, my_address = line.strip().split(",")
                mycontacts.append({"name": my_name, "number": my_number, "email": my_email, "address": my_address})
    except FileNotFoundError:
        pass
    return mycontacts

def saveContacts(mycontacts):
    with open("mycontacts.txt", "w") as file:
        for contact in mycontacts:
            file.write(f"{contact['name']},{contact['number']},{contact['email']},{contact['address']}\n")

def addContact(mycontacts):
    name = input("Enter name to insert: ")
    number = input("Enter number to insert: ")
    email = input("Enter email to insert: ")
    address = input("Enter address to insert: ")
    mycontacts.append({"name": name, "number": number, "email": email, "address": address})

def deleteContact(mycontacts):
    index = int(input("Enter contact number to delete: "))
    if 1 <= index <= len(mycontacts):
        del mycontacts[index - 1]
        print("Contact deleted successfully")
    else:
        print("Invalid contact")

def viewContacts(mycontacts):
    table = PrettyTable(["S.no", "Name", "Number", "Email", "Address"])
    print("\nMy Contacts list:")
    print("-----------------")
    if not mycontacts:
        print("No contacts")
    else:
        for i, contact in enumerate(mycontacts, 1):
            table.add_row([i, contact['name'], contact['number'], contact['email'], contact['address']])
    print(table,"\n")
def searchContact(mycontacts):
    contact = input("Enter name to search: ")
    found = False
    for i in range(len(mycontacts)):
        if mycontacts[i]["name"] == contact:
            print("Contact found:", mycontacts[i])
            found = True
            break
    if not found:
        print("Contact not found")

def updateContact(mycontacts):
    index = int(input("Enter index of contact to update: ")) - 1
    if 0 <= index < len(mycontacts):
        print("Current Contact Details:")
        print("Name:", mycontacts[index]["name"])
        print("Number:", mycontacts[index]["number"])
        print("Email:", mycontacts[index]["email"])
        print("Address:", mycontacts[index]["address"])
        mycontacts[index]["name"] = input("Enter updated name: ")
        mycontacts[index]["number"] = input("Enter updated number: ")
        mycontacts[index]["email"] = input("Enter updated email: ")
        mycontacts[index]["address"] = input("Enter updated address: ")
        
        print("Contact updated successfully!")
    else:
        print("Invalid index.")

def main():
    mycontacts = loadContacts()
    while True:
        print("Contact Operations")
        print("------------------")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Update Contact")
        print("6. Close")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            addContact(mycontacts)
            saveContacts(mycontacts)
        elif ch == 2:
            viewContacts(mycontacts)
        elif ch == 3:
            searchContact(mycontacts)
        elif ch == 4:
            deleteContact(mycontacts)
            saveContacts(mycontacts)
        elif ch == 5:
            updateContact(mycontacts)
            saveContacts(mycontacts)
        elif ch == 6:
            print("Closing....")
            break
        else:
            print("Invalid choice. Please choose again")

if __name__ == "__main__":
    main()
