marks = []
for i in range(5):
    marks.append(int(input(f"Enter subject {i+1} marks: ")))

total = sum(marks)
percentage = total / 5

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
