salary = int(input("Enter monthly salary: "))
age = int(input("Enter age: "))
experience = int(input("Enter years of experience: "))

if age >= 21 and salary >= 25000 and experience >= 2:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")
