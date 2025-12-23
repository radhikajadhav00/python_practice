balance = 2000

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = int(input("Choose: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amt = int(input("Enter amount: "))
        balance += amt
        print("Deposited!")

    elif choice == 3:
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn!")
        else:
            print("Insufficient balance")

    else:
        break
