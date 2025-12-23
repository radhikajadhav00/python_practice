import random
import string

def generate_password(length=12):
    # characters used in password
    letters = string.ascii_letters     # A-Z + a-z
    digits = string.digits             # 0-9
    symbols = string.punctuation       # special characters

    # combine all
    all_chars = letters + digits + symbols

    # generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


# ----------------------------
# Main Program
# ----------------------------
print("🔐 Password Generator")
user_length = int(input("Enter password length (e.g., 8, 12, 16): "))
strong_password = generate_password(user_length)

print("\nYour generated password is:")
print(strong_password)
