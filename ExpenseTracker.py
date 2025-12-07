expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added!")

def show_expenses():
    print("\n--- Expense List ---")
    total = 0
    for e in expenses:
        print(f"{e['category']} : ₹{e['amount']}")
        total += e['amount']
    print("Total Expense:", total)

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = int(input("Choose: "))
    if choice == 1:
        add_expense()
    elif choice == 2:
        show_expenses()
    else:
        break
