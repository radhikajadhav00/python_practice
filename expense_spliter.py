total = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

share = total / people
print("Each person should pay:", round(share, 2))
