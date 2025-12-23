import random
import string

url = input("Enter a URL: ")

short_code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
short_url = "short.ly/" + short_code

print("Short URL:", short_url)
