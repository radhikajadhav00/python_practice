num1 =int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))
num3 =int(input("Enter third Number:"))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")