marks = list(map(int, input("Enter marks of 5 subjects: ").split()))

average = sum(marks) / len(marks)

if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Average:", average)
print("Grade:", grade)
