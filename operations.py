def calculation(num1,num2):
    print("Add:",num1+num2)
    print("Subtraction:",num1-num2)
    print("multiplication:",num1*num2)
    if num2!=0:
        print("Division:",num1/num2)
    else:
        print("Error: Divisible by zero is not allowed...")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
calculation(num1,num2)
