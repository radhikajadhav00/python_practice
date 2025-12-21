contacts = {}

name = input("Enter name: ")
phone = input("Enter phone number: ")

contacts[name] = phone

print("Saved Contacts:")
for k, v in contacts.items():
    print(k, ":", v)
