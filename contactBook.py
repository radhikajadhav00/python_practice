contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Exit")
    choice = int(input("Choose: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number
        print("Contact saved!")

    elif choice == 2:
        print("\n--- Contact List ---")
        for name, number in contacts.items():
            print(name, ":", number)

    else:
        print("Goodbye!")
        break
