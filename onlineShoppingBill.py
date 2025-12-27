total = 0

while True:
    price = int(input("Enter item price (0 to stop): "))
    if price == 0:
        break
    total += price

discount = 0
if total >= 5000:
    discount = total * 0.2
elif total >= 3000:
    discount = total * 0.1

final_amount = total - discount

print("Total Bill:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
