import random

while True:
    roll = random.randint(1, 6)
    print("Dice rolled:", roll)

    again = input("Roll again? (y/n): ")
    if again.lower() != "y":
        break
