day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid Date")
elif month == 2:
    if day >= 1 and day <= 28:
        print("Valid Date")
    else:
        print("Invalid Date")
elif month in [4, 6, 9, 11]:
    if day >= 1 and day <= 30:
        print("Valid Date")
    else:
        print("Invalid Date")
else:
    if day >= 1 and day <= 31:
        print("Valid Date")
    else:
        print("Invalid Date")
