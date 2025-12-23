import random

hex_digits = "0123456789ABCDEF"

color = "#"
for _ in range(6):
    color += random.choice(hex_digits)

print("Random Color Code:", color)
