def is_greater(a,b):
    if a>b:
        print(f"The greater number is : {a}")
    elif a<b:
        print(f"The greater number is : {b}")
    else:
        print("Both numbers are equal")
    
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

is_greater(num1,num2)