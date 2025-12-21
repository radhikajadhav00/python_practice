score = 0

print("Quiz: Python Basics")

answer = input("What keyword is used to define a function? ")
if answer.lower() == "def":
    score += 1

answer = input("Which data type stores True/False? ")
if answer.lower() == "boolean" or answer.lower() == "bool":
    score += 1

print("Your score:", score, "/2")
