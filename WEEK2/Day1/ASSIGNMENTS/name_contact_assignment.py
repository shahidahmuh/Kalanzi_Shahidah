contacts = []

def validPhone(phone):
    for char in phone:
        if not (char.isdigit() or char == "-" or char == "+"):
            return False
    return True

def validEmail(email):
    if email == "":
        return True
    return "@" in email and "." in email

#Add Contact
def addContact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    if not validPhone(phone):
        print("Invalid Phone Number!!")
        return
    if not validEmail(email):
        print("Invalid Email!!")
        return
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print("Contact added successfully.")

    #View Contacts
def viewContacts():
        if not contacts:
            print ("No Contacts Found")
            return
        
        for index, contact in enumerate(contacts, start=1):
            print(f"\nContact {index}")
            print(f"Name : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")
    
    #Update Contact
def updateContact():
        name = input("Enter Contact name: ")
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                newPhone = input("New Phone : ")
                newEmail = input("New Email ;")
                if not validPhone(newPhone):
                    print ("Invalid phone number!!")
                    return
                if not validEmail(newEmail):
                    print("Invalid Email!!")
                    return
                
                contact["phone"] = newPhone
                contact["email"] = newEmail
                print("Contact Updated Successfully.")
                return
        print("Contact Not Found!!")

#Delete Contact
def deleteContact():
    name = input ("Enter contact name to delete:")
    
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print ('Contact deleted successfully.')
            return
    print("Contact Not Found.")

#Search Contacts 
def searchContacts():
    keyword = input("Search by Name, Phone or Email: ").lower()
    results = []

    for contact in contacts:
        if (keyword in contact["name"].lower()
            or keyword in contact["phone"].lower()
            or keyword in contact["email"].lower()):
            results.append(contact)

    if not results:
        print("No Matching contacts Found.")
        return
    
    print ("\nSearch Results")

    for contact in results:
        print(f"Name : {contact['name']}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")

#List of allcontacts 
def listContacts():
    viewContacts()

def Main():
    while True:

        print("\n CONTACT MANAGER MENU")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            addContact()
        elif choice == "2":
            viewContacts()
        elif choice == "3":
            updateContact()
        elif choice == "4":
            deleteContact()
        elif choice == "5":
            searchContacts()
        elif choice == "6":
            listContacts()
        elif choice == "7":
            print("Exit: GoodBye!")
        else:
            print("Invalod Option. Try Again!")
Main()    
        



