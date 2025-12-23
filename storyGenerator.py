import random

names = ["Ravi", "Sneha", "Amit", "Pooja"]
places = ["Mumbai", "Pune", "Nashik", "Delhi"]
actions = ["found a treasure", "solved a mystery", "built a robot", "won a prize"]

story = f"{random.choice(names)} went to {random.choice(places)} and {random.choice(actions)}."
print(story)
