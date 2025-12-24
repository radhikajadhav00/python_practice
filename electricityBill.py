units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = units * 2
else:
    bill = units * 3

print("Electricity Bill = ₹", bill)
