import random

names = ["tech", "code", "dev", "python", "it"]
number = random.randint(100, 999)

username = random.choice(names) + str(number)
print("Generated username:", username)
