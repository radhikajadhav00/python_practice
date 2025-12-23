taken_usernames = ["admin", "user", "test", "python"]

username = input("Enter username: ")

if username.lower() in taken_usernames:
    print("Username already taken")
else:
    print("Username is available")
