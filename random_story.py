import random

characters = ["A coder", "A student", "An engineer"]
places = ["in a lab", "at college", "at home"]
actions = ["built an app", "fixed a bug", "learned Python"]

story = f"{random.choice(characters)} {random.choice(actions)} {random.choice(places)}."
print(story)
