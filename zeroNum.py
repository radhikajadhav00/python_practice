# num=int(input("Enter number want to check: "))
# if num==0:
#     print("The number is zero")
# else:
#     print("The number is NOT zero")



def is_zero(number):
    if number==0:
        return True
    else:
        return False
    
num=int(input("enter any number:"))
# num2=int(input("Enter second number:"))
# print(f"{num1} is zero: {is_zero(num1)}")
print(f"{num} is zero: {is_zero(num)}")
