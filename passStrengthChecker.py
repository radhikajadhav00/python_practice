password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if 'A' <= ch <= 'Z':
        has_upper = True
    elif 'a' <= ch <= 'z':
        has_lower = True
    elif '0' <= ch <= '9':
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Strong Password")
else:
    print("Weak Password")
