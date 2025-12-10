msg = input("Enter reminder message: ")

with open("reminder.txt", "w") as f:
    f.write(msg)

print("Reminder saved in reminder.txt")
